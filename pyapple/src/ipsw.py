from typing import List

from ..interface import IPSW, OTAIPSW, IPSWKeys, Keys, iDevice
from ..utils import AsyncRequest


class IPSW:
    def __init__(self) -> None:
        self.HTTP = AsyncRequest()
        super().__init__()

    async def fetch_device(self, identifier: str) -> iDevice:
        data = await self.HTTP.ipsw(
            endpoint=f"/device/{identifier}", return_type="json"
        )
        data["firmwares"] = [IPSW(**firmware) for firmware in data["firmwares"]]

        return iDevice(**data)

    async def search_ipsw(self, identifier: str, buildid: str) -> IPSW:
        data = await self.HTTP.ipsw(
            endpoint=f"/ipsw/{identifier}/{buildid}", return_type="json"
        )

        return IPSW(**data)

    async def fetch_ipsw_version(self, version: str) -> List:
        data = await self.HTTP.ipsw(endpoint=f"/ipsw/{version}", return_type="json")

        return [IPSW(**firmware) for firmware in data]

    async def device_keys(self, identifier: str) -> List:
        data = await self.HTTP.ipsw(
            endpoint=f"/keys/device/{identifier}", return_type="json"
        )

        return [IPSWKeys(**keys) for keys in data]

    async def firmware_keys(self, identifier: str, buildid: str) -> IPSWKeys:
        data = await self.HTTP.ipsw(
            endpoint=f"/keys/ipsw/{identifier}/{buildid}", return_type="json"
        )
        data["keys"] = [Keys(**keys) for keys in data["keys"]]

        return IPSWKeys(**data)

    async def search_ota(self, identifier: str, buildid: str) -> OTAIPSW:
        data = await self.HTTP.ipsw(
            endpoint=f"/ota/{identifier}/{buildid}", return_type="json"
        )

        return OTAIPSW(**data)

    async def fetch_ota_version(self, version: str) -> List:
        data = await self.HTTP.ipsw(endpoint=f"/ota/{version}", return_type="json")

        return [OTAIPSW(**ota) for ota in data]

    async def fetch_ota_docs(self, identifier: str, version: str) -> str:
        data = await self.HTTP.ipsw(
            endpoint=f"/ota/documentation/{identifier}/{version}", return_type="text"
        )

        return data
