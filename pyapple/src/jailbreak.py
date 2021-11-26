from typing import Dict, List

from ..interface import Builds, Repo, Tweak
from ..utils import AsyncRequest


class Jailbreak:
    """Class for jailbreak related functions."""

    def __init__(self) -> None:
        self.__HTTP = AsyncRequest()
        super().__init__()

    def __filter_keys(self, key: str) -> str:
        key = key.lower()
        key = key.replace("-", "_")
        return key

    def __lower_keys(self, data) -> Dict:
        return {self.__filter_keys(key): value for key, value in data.items()}

    async def fetch_repo(self, url: str) -> Repo:
        """Fetches some information about a repo.

        Args:
            url (str): URL of the repo.

        Returns:
            Repo: Dataclass object of the repo.
        """

        data = await self.__HTTP.parcility(endpoint=f"/?url={url}")
        data = self.__lower_keys(data)

        await self.__HTTP.session.close()
        return Repo(**data)

    async def search_repo(self, slug: str) -> Repo:
        """Searches repositories from Parcility API.

        Args:
            slug (str): repository keyword to search.

        Returns:
            Repo: Dataclass object of the repo.
        """

        data = await self.__HTTP.parcility(endpoint=f"/db/repo/{slug}")
        data = self.__lower_keys(data)

        await self.__HTTP.session.close()
        return Repo(**data)

    async def fetch_tweak(self, bundle_id: str) -> Tweak:
        """Fetches tweak from Parcility API.

        Args:
            bundle_id (str): Tweak bundle id to fetch.

        Returns:
            Tweak: Dataclass object of the tweak.
        """

        data = await self.__HTTP.parcility(endpoint=f"/db/package/{bundle_id}")
        data = self.__lower_keys(data)

        data["builds"] = [self.__lower_keys(build) for build in data["builds"]]
        data["builds"] = [Builds(**build) for build in data["builds"]]
        data["depends"] = data["depends"].split(", ")

        await self.__HTTP.session.close()
        return Tweak(**data)

    async def search_tweak(
        self,
        query: str,
        repo: str = "all",
        section: str = "Tweaks",
        field: str = "Name",
    ) -> List[Tweak]:
        """Searches tweak from Parcility API.

        Args:
            query (str): Keyword to search.
            repo (str, optional): Specific repository to search. Defaults to "all".
            section (str, optional): Specific tweak section to search. Defaults to "Tweaks".
            field (str, optional): Specific tweak field to search. Defaults to "Name".

        Returns:
            List[Tweak]: [description]
        """

        data = await self.__HTTP.parcility(
            endpoint=f"/db/search?q={query}&repo={repo}&section={section}&field={field}"
        )

        for index in range(len(data)):
            data[index] = self.__lower_keys(data[index])

            data[index]["builds"] = [
                self.__lower_keys(build) for build in data[index]["builds"]
            ]
            data[index]["builds"] = [Builds(**build) for build in data[index]["builds"]]
            data[index]["depends"] = data[index]["depends"].split(", ")

        await self.__HTTP.session.close()
        return [Tweak(**tweaks) for tweaks in data]
