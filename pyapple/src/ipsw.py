from typing import List

from ..interface import IPSW, OTAIPSW, IPSWKeys, Keys, iDevice
from ..utils import AsyncRequest


class IPSW:
    def __init__(self) -> None:
        self.HTTP = AsyncRequest()
        super().__init__()

    async def device(self, identifier: str) -> iDevice:
        data = await self.HTTP.ipsw(endpoint=f"/device/{identifier}")
        data["firmwares"] = [IPSW(**firmware) for firmware in data["firmwares"]]

        return iDevice(**data)

    async def ipsw(self, identifier: str, buildid: str) -> IPSW:
        data = await self.HTTP.ipsw(endpoint=f"/ipsw/{identifier}/{buildid}")

        return IPSW(**data)

    async def ipsw_version(self, version: str) -> List:
        data = await self.HTTP.ipsw(endpoint=f"/ipsw/{version}")

        return [IPSW(**firmware) for firmware in data]

    async def keys_device(self, identifier: str) -> List:
        data = await self.HTTP.ipsw(endpoint=f"/keys/device/{identifier}")

        return [IPSWKeys(**keys) for keys in data]

    async def keys(self, identifier: str, buildid: str) -> IPSWKeys:
        data = await self.HTTP.ipsw(endpoint=f"/keys/ipsw/{identifier}/{buildid}")
        data["keys"] = [Keys(**keys) for keys in data["keys"]]

        return IPSWKeys(**data)

    async def ota(self, identifier: str, buildid: str) -> OTAIPSW:
        data = await self.HTTP.ipsw(endpoint=f"/ota/{identifier}/{buildid}")

        return OTAIPSW(**data)

    async def ota_version(self, version: str) -> List:
        data = await self.HTTP.ipsw(endpoint=f"/ota/{version}")

        return [OTAIPSW(**ota) for ota in data]

    async def ota_docs(self, identifier: str, version: str):
        data = await self.HTTP.ipsw(
            endpoint=f"/ota/documentation/{identifier}/{version}",
            headers={"Content-Type": "application/json"},
        )

        print(data)
