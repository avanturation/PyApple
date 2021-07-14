from typing import Dict, List

from ..interface import Builds, Repo, Tweak
from ..utils import AsyncRequest


class Cydia:
    def __init__(self) -> None:
        self.__HTTP = AsyncRequest()
        super().__init__()

    def __lower_keys(self, data) -> Dict:
        return {key.lower(): value for key, value in data}

    async def fetch_repo(self, url: str) -> Repo:
        data = await self.__HTTP.cydia(endpoint=f"/?url={url}")
        data = self.__lower_keys(data)

        return Repo(**data)

    async def search_repo(self, slug: str) -> Repo:
        data = await self.__HTTP.cydia(endpoint=f"/db/repo/{slug}")
        data = self.__lower_keys(data)

        return Repo(**data)

    async def fetch_tweak(self, bundle_id: str, return_depends: bool = False) -> Tweak:
        data = await self.__HTTP.cydia(endpoint=f"/db/package/{bundle_id}")
        data = self.__lower_keys(data)

        data["builds"] = [self.__lower_keys(build) for build in data["builds"]]
        data["builds"] = [Builds(**build) for build in data["builds"]]

        if return_depends:
            pass  # future

        return Tweak(**data)

    async def search_tweak(
        self,
        query: str,
        repo: str = "all",
        section: str = "Tweaks",
        field: str = "Name",
        return_depends: bool = False,
    ) -> List[Tweak]:
        data = await self.__HTTP.cydia(
            endpoint=f"/db/search?q={query}&repo={repo}&section={section}&field={field}"
        )
        for index in range(len(data)):
            data[index] = self.__lower_keys(data[index])

            data[index]["builds"] = [
                self.__lower_keys(build) for build in data[index]["builds"]
            ]
            data[index]["builds"] = [Builds(**build) for build in data[index]["builds"]]

            if return_depends:
                pass  # future

        return data
