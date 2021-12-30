import plistlib
import re
from contextlib import suppress
from typing import List, Optional, Literal, Dict
from asyncio import gather

from ..interface import MacOSProduct, Package, NoCatalogResult
from ..utils import Requester

OSINSTALL = {
    "User-Agent": "osinstallersetupplaind (unknown version) CFNetwork/720.5.7 Darwin/14.5.0 (x86_64)"
}
SWUPDATE = {
    "User-Agent": "Software%20Update (unknown version) CFNetwork/807.0.1 Darwin/16.0.0 (x86_64)"
}

CATLOG_SUF = {
    "publicbeta": "beta",  # Apple Beta Software Program
    "publicrelease": "",  # Public Release (most of users)
    "customerseed": "customerseed",
    "developerbeta": "seed",  # Developer Beta, which you can get from betaprofiles.com
}

MACOS_NAME = {
    "8": "mountainlion",
    "7": "lion",
    "6": "snowleopard",
    "5": "leopard",
}

CATLOG_SUF_TYPING = Literal[
    "publicbeta", "publicrelease", "customerseed", "developerbeta"
]


class SWSCAN(Requester):
    """Class for SWSCAN related functions."""

    def __init__(self):
        self.root: Optional[Dict] = {}
        self.min_macos = 5
        self.max_macos = 16
        super().__init__()

    def __build_url(self, catalog_id: str) -> str:
        catalog = catalog_id.lower()
        url = "https://swscan.apple.com/content/catalogs/others/index-12"

        if CATLOG_SUF[catalog]:
            url = url.replace("12", "12" + CATLOG_SUF[catalog] + "-12-")

        url += "-".join(
            [
                MACOS_NAME[str(x)] if str(x) in MACOS_NAME else "10." + str(x)
                for x in reversed(range(self.min_macos, self.max_macos + 1))
            ]
        )

        url += ".merged-1.sucatalog"

        return url

    async def fetch_catalog(
        self, catalog_id: Optional[CATLOG_SUF_TYPING] = "publicrelease"
    ):
        """Fetches swscan catalog from Apple server.

        Args:
            catalog_id (Literal["publicbeta", "publicrelease", "customerseed", "developerbeta"], optional): Catalog ID to fetch. Defaults to "publicrelease".

        Returns:
            Dict: Catalog plist object by loaded by plistlib
        """

        raw_catalog = await self.swscan(
            self.__build_url(catalog_id), headers=OSINSTALL, return_type="text"
        )
        catalog_data = bytes(raw_catalog, "utf-8")
        self.root[catalog_id] = plistlib.loads(catalog_data)

        return self.root[catalog_id]

    async def __valid_products(
        self, catalog_id="publicrelease", fetch_recovery: bool = False
    ):
        if not catalog_id in self.root:
            await self.fetch_catalog(catalog_id)

        if not fetch_recovery:
            return [
                p
                for p in self.root[catalog_id].get("Products", {})
                if self.root[catalog_id]
                .get("Products", {})
                .get(p, {})
                .get("ExtendedMetaInfo", {})
                .get("InstallAssistantPackageIdentifiers", None)
            ]

        else:
            return [
                p
                for p in self.root[catalog_id].get("Products", {})
                if any(
                    x
                    for x in self.root[catalog_id]
                    .get("Products", {})
                    .get(p, {})
                    .get("Packages", [])
                    if x["URL"].endswith(
                        ("RecoveryHDUpdate.pkg", "RecoveryHDMetaDmg.pkg")
                    )
                )
            ]

    async def fetch_product(
        self, product_id: str, catalog_id: Optional[CATLOG_SUF_TYPING] = "publicrelease"
    ) -> Dict:
        """Returns a product by its id.

        Args:
            product_id (str): Product ID to fetch.
            catalog_id (Literal["publicbeta", "publicrelease", "customerseed", "developerbeta"], optional): Swscan channel to fet. Defaults to "publicrelease".

        Raises:
            NoCatalogResult: If there is no result, raises NoCatalogResult.

        Returns:
            Dict: A dictonary of the product.
        """
        if not catalog_id in self.root:
            await self.fetch_catalog(catalog_id)

        try:
            return self.root[catalog_id]["Products"][product_id]

        except KeyError:
            raise NoCatalogResult(product_id)

    async def fetch_macos(
        self,
        catalog_id: Optional[CATLOG_SUF_TYPING] = "publicrelease",
        fetch_recovery: bool = False,
    ) -> List[MacOSProduct]:
        """Fetches all available macOS from Apple server.

        Args:
            catalog_id (Literal["publicbeta", "publicrelease", "customerseed", "developerbeta"], optional): Catalog ID to fetch. Defaults to "publicrelease".
            fetch_recovery (bool, optional): Fetches only Recovery. Defaults to False.

        Returns:
            List[MacOSProduct]: List of dataclass objects of macOS Product
        """

        if not not catalog_id in self.root:
            await self.fetch_catalog(catalog_id)

        vaild_ids = await self.__valid_products(catalog_id, fetch_recovery)

        tasks = [
            self.__create_product(product_id, catalog_id) for product_id in vaild_ids
        ]
        results = await gather(*tasks)

        return results

    async def search_macos(
        self,
        version: Optional[str],
        catalog_id: Optional[CATLOG_SUF_TYPING] = "publicrelease",
        fetch_recovery: bool = False,
    ) -> List[MacOSProduct]:
        """Returns macOS Product by its version.

        Args:
            version (Optional[str]): macOS version to search. (e.g. 11.5)
            catalog_id (Literal["publicbeta", "publicrelease", "customerseed", "developerbeta"], optional): Catalog ID to fetch. Defaults to "publicrelease".
            fetch_recovery (bool, optional): Fetches only Recovery. Defaults to False.

        Returns:
            List[MacOSProduct]: List of dataclass objects of macOS Product
        """

        if not not catalog_id in self.root:
            await self.fetch_catalog(catalog_id)

        vaild_ids = await self.__valid_products(catalog_id, fetch_recovery)

        tasks = [
            self.__create_product(product_id, catalog_id) for product_id in vaild_ids
        ]
        results = await gather(*tasks)

        return list(filter(lambda product: product.version == version, results))

    async def __create_product(
        self, product_id: str, catalog_id="publicrelease"
    ) -> MacOSProduct:
        if not not catalog_id in self.root:
            await self.fetch_catalog(catalog_id)

        try:
            resp = await self.request(
                method="GET",
                url=self.root["Products"][product_id]["ServerMetadataURL"],
                return_type="text",
            )

            smd = plistlib.loads(bytes(resp, "utf-8"))
            name = smd["localization"]["English"]["title"]
            version = smd["CFBundleShortVersionString"]

            dist_file = await self.request(
                method="GET",
                url=self.root["Products"][product_id]["Distributions"]["English"],
                return_type="text",
            )

            build_search = (
                "macOSProductBuildVersion"
                if "macOSProductBuildVersion" in dist_file
                else "BUILD"
            )

            with suppress(Exception):
                build = (
                    dist_file.split("<key>{}</key>".format(build_search))[1]
                    .split("<string>")[1]
                    .split("</string>")[0]
                )

        except:
            dist_file = await self.request(
                url=self.root["Products"][product_id]["Distributions"]["English"],
                method="GET",
                return_type="text",
            )

            build_search = (
                "macOSProductBuildVersion"
                if "macOSProductBuildVersion" in dist_file
                else "BUILD"
            )

            vers_search = (
                "macOSProductVersion"
                if "macOSProductVersion" in dist_file
                else "VERSION"
            )

            with suppress(Exception):
                build = (
                    dist_file.split("<key>{}</key>".format(build_search))[1]
                    .split("<string>")[1]
                    .split("</string>")[0]
                )

            with suppress(Exception):
                version = (
                    dist_file.split("<key>{}</key>".format(vers_search))[1]
                    .split("<string>")[1]
                    .split("</string>")[0]
                )

            with suppress(Exception):
                name = re.search(r"<title>(.+?)</title>", dist_file).group(1)

        mapping = {
            "product_id": product_id,
            "title": name,
            "version": version,
            "buildid": build,
            "postdate": self.root.get("Products", {})
            .get(product_id, {})
            .get("PostDate", ""),
            "packages": [
                Package(url=package["URL"], filesize=package["Size"])
                for package in self.root["Products"][product_id]["Packages"]
            ],
        }

        return MacOSProduct(**mapping)
