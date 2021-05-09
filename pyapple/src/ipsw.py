from typing import List

from ..interface import IPSW, OTAIPSW, IPSWKeys, Keys, iDevice
from ..utils import AsyncRequest


class IPSWStuff:
    def __init__(self) -> None:
        pass

    @staticmethod
    async def device(identifier: str) -> iDevice:
        data = await AsyncRequest.ipsw(method="GET", endpoint=f"/device/{identifier}")
        data["firmwares"] = [IPSW(**firmware) for firmware in data["firmwares"]]

        return iDevice(**data)

    @staticmethod
    async def ipsw(identifier: str, buildid: str) -> IPSW:
        data = await AsyncRequest.ipsw(
            method="GET", endpoint=f"/ipsw/{identifier}/{buildid}"
        )

        return IPSW(**data)

    @staticmethod
    async def ipsw_version(version: str) -> List:
        data = await AsyncRequest.ipsw(method="GET", endpoint=f"/ipsw/{version}")

        return [IPSW(**firmware) for firmware in data]

    @staticmethod
    async def keys_device(identifier: str) -> List:
        data = await AsyncRequest.ipsw(
            method="GET", endpoint=f"/keys/device/{identifier}"
        )

        return [IPSWKeys(**keys) for keys in data]

    @staticmethod
    async def keys(identifier: str, buildid: str) -> IPSWKeys:
        data = await AsyncRequest.ipsw(
            method="GET", endpoint=f"/keys/ipsw/{identifier}/{buildid}"
        )
        data["keys"] = [Keys(**keys) for keys in data["keys"]]

        return IPSWKeys(**data)

    @staticmethod
    async def ota(identifier: str, buildid: str) -> OTAIPSW:
        data = await AsyncRequest.ipsw(
            method="GET", endpoint=f"/ota/{identifier}/{buildid}"
        )

        return OTAIPSW(**data)

    @staticmethod
    async def ota_version(version: str) -> List:
        data = await AsyncRequest.ipsw(method="GET", endpoint=f"/ota/{version}")

        return [OTAIPSW(**ota) for ota in data]
