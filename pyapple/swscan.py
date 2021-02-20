import plistlib
import re
from typing import Optional

from .model import IntelMacOS, IntelMacOSPkg
from .parser import Parser

MIN_MACOS = 5
MAX_MACOS = 16

OSINSTALL = {
    "User-Agent": "osinstallersetupplaind (unknown version) CFNetwork/720.5.7 Darwin/14.5.0 (x86_64)"
}
SWUPDATE = {
    "User-Agent": "Software%20Update (unknown version) CFNetwork/807.0.1 Darwin/16.0.0 (x86_64)"
}

CATLOG_SUF = {
    "publicseed": "beta",
    "publicrelease": "",
    "customerseed": "customerseed",
    "developerseed": "seed",
}

MACOS_NAME = {
    "8": "mountainlion",
    "7": "lion",
    "6": "snowleopard",
    "5": "leopard",
}

MACOS_FULLNAME = {
    "tiger": "10.4",
    "leopard": "10.5",
    "snow leopard": "10.6",
    "lion": "10.7",
    "mountain lion": "10.8",
    "mavericks": "10.9",
    "yosemite": "10.10",
    "el capitan": "10.11",
    "sierra": "10.12",
    "high sierra": "10.13",
    "mojave": "10.14",
    "catalina": "10.15",
    "big sur": "10.16",
}


class SWSCAN:
    def __init__(self):
        self.HTTP = Parser()  # 커스텀 리퀘스트 보내는 클래스 - aiohttp 사용
        self.recovery_suffixes = ("RecoveryHDUpdate.pkg", "RecoveryHDMetaDmg.pkg")
        self.min_macos = MIN_MACOS
        self.max_macos = MAX_MACOS
        self.macos_dict = []

    def build_url(self, catalog_id="DeveloperSeed") -> str:
        catalog = catalog_id.lower()
        version = self.max_macos
        url = "https://swscan.apple.com/content/catalogs/others/index-"

        url += "-".join(
            [
                MACOS_NAME[str(x)] if str(x) in MACOS_NAME else "10." + str(x)
                for x in reversed(range(self.min_macos, version + 1))
            ]
        )

        url += ".merged-1.sucatalog"
        ver_s = (
            MACOS_NAME[str(version)]
            if str(version) in MACOS_NAME
            else "10." + str(version)
        )

        if len(CATLOG_SUF[catalog]):
            url = url.replace(ver_s, ver_s + CATLOG_SUF[catalog] + "-" + ver_s)

        return url

    async def fetch_catalog(self, catalog_id="publicseed") -> bytes:
        url = self.build_url(catalog_id)
        self.raw_catalog = await self.HTTP.request(url, header=OSINSTALL)
        self.catalog_data = bytes(self.raw_catalog, "utf-8")
        self.root = plistlib.loads(self.catalog_data)
        return self.root

    async def get_products(self, catalog_id="publicseed"):
        self.macos_dict = []
        if not hasattr(self, "root"):
            await self.fetch_catalog(catalog_id)

        products = self.root["Products"]
        for product in products:
            if "ExtendedMetaInfo" in products[product]:
                IAMetaInfo = products[product]["ExtendedMetaInfo"]

                if "InstallAssistantPackageIdentifiers" in IAMetaInfo:
                    IAPackageID = IAMetaInfo["InstallAssistantPackageIdentifiers"]

                    if "OSInstall" in IAPackageID:
                        if IAPackageID["OSInstall"] == "com.apple.mpkg.OSInstall":
                            obj = IntelMacOS(product)
                            await self.get_metadata(product, obj)
                            self.macos_dict.append(obj)

                    if "SharedSupport" in IAPackageID:
                        if IAPackageID["SharedSupport"].startswith(
                            "com.apple.pkg.InstallAssistant"
                        ):
                            obj = IntelMacOS(product)
                            await self.get_metadata(product, obj)
                            self.macos_dict.append(obj)

            if "Packages" in products[product]:
                Packages = products[product]["Packages"]

                if "URL" in Packages:
                    URL = Packages["URL"]

                    for obj in self.recovery_suffixes:
                        if URL.endswith(obj):
                            obj = IntelMacOS(product)
                            await self.get_metadata(product, obj)
                            self.macos_dict.append(obj)

            return self.macos_dict

    async def get_package(
        self,
        build_id: Optional[str],
        version: Optional[str],
        product_id: Optional[str],
        catalog_id="publicseed",
    ):
        self.macos_dict = []
        if not hasattr(self, "root"):
            await self.fetch_catalog(catalog_id)

        products = self.root["Products"]
        for product in products:
            if "ExtendedMetaInfo" in products[product]:
                IAMetaInfo = products[product]["ExtendedMetaInfo"]

                if "InstallAssistantPackageIdentifiers" in IAMetaInfo:
                    IAPackageID = IAMetaInfo["InstallAssistantPackageIdentifiers"]

                    if "OSInstall" in IAPackageID:
                        if IAPackageID["OSInstall"] == "com.apple.mpkg.OSInstall":
                            obj = IntelMacOS(product)
                            await self.get_metadata(product, obj)

                            if obj.build == build_id:
                                await self.append_pkg(product, obj)
                                self.macos_dict.append(obj)

                            elif obj.version == version:
                                await self.append_pkg(product, obj)
                                self.macos_dict.append(obj)

                            elif obj.product_id == product_id:
                                await self.append_pkg(product, obj)
                                self.macos_dict.append(obj)

                    if "SharedSupport" in IAPackageID:
                        if IAPackageID["SharedSupport"].startswith(
                            "com.apple.pkg.InstallAssistant"
                        ):
                            obj = IntelMacOS(product)
                            await self.get_metadata(product, obj)

                            if obj.build == build_id:
                                await self.append_pkg(product, obj)
                                self.macos_dict.append(obj)

                            elif obj.version == version:
                                await self.append_pkg(product, obj)
                                self.macos_dict.append(obj)

                            elif obj.product_id == product_id:
                                await self.append_pkg(product, obj)
                                self.macos_dict.append(obj)

            if "Packages" in products[product]:
                Packages = products[product]["Packages"]

                if "URL" in Packages:
                    URL = Packages["URL"]
                    for obj in self.recovery_suffixes:
                        if URL.endswith(obj):
                            obj = IntelMacOS(product)
                            await self.get_metadata(product, obj)

                            if obj.build == build_id:
                                await self.append_pkg(product, obj)
                                self.macos_dict.append(obj)

                            elif obj.version == version:
                                await self.append_pkg(product, obj)
                                self.macos_dict.append(obj)

                            elif obj.product_id == product_id:
                                await self.append_pkg(product, obj)
                                self.macos_dict.append(obj)

            return self.macos_dict

    async def get_metadata(self, product, object: IntelMacOS):
        target = self.root["Products"][product]

        try:
            resp = await self.HTTP.request(target["ServerMetadataURL"])
            smd = plistlib.loads(bytes(resp, "utf-8"))

            object.title = smd["localization"]["English"]["title"]
            object.version = smd["CFBundleShortVersionString"]

            dist_file = await self.HTTP.request(target["Distributions"]["English"])
            build = version = name = "Unknown"

            build_search = (
                "macOSProductBuildVersion"
                if "macOSProductBuildVersion" in dist_file
                else "BUILD"
            )

            try:
                build = (
                    dist_file.split("<key>{}</key>".format(build_search))[1]
                    .split("<string>")[1]
                    .split("</string>")[0]
                )
            except:
                pass

            object.build = build

        except KeyError:
            dist_file = await self.HTTP.request(target["Distributions"]["English"])
            build = version = name = "Unknown"

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

            try:
                build = (
                    dist_file.split("<key>{}</key>".format(build_search))[1]
                    .split("<string>")[1]
                    .split("</string>")[0]
                )
            except:
                pass

            try:
                version = (
                    dist_file.split("<key>{}</key>".format(vers_search))[1]
                    .split("<string>")[1]
                    .split("</string>")[0]
                )
            except:
                pass

            try:
                name = re.search(r"<title>(.+?)</title>", dist_file).group(1)
            except:
                pass

            object.build = build
            object.title = name
            object.version = version

    async def append_pkg(self, product, object: IntelMacOS):
        target = self.root["Products"][product]
        for package in target["Packages"]:
            full_pkg = IntelMacOSPkg(url=package["URL"], filesize=package["Size"])
            object.packages.append(full_pkg)
