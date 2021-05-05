import asyncio
import functools
from typing import Any, List, Optional

from .model import IPSW, OTAIPSW, IPSWKeys, KeysObject, iDevice
from .parser import Parser
from .swscan import SWSCAN

SWSCAN = SWSCAN()


class RealClient:
    def __init__(self) -> None:
        pass

    @staticmethod
    async def device(identifier: str) -> iDevice:
        data = await Parser.ipsw(method="GET", endpoint=f"/device/{identifier}")
        data["firmwares"] = [IPSW(**firmware) for firmware in data["firmwares"]]

        return iDevice(**data)

    @staticmethod
    async def ipsw(identifier: str, buildid: str) -> IPSW:
        data = await Parser.ipsw(method="GET", endpoint=f"/ipsw/{identifier}/{buildid}")

        return IPSW(**data)

    @staticmethod
    async def ipsw_version(version: str) -> List:
        data = await Parser.ipsw(method="GET", endpoint=f"/ipsw/{version}")

        return [IPSW(**firmware) for firmware in data]

    @staticmethod
    async def keys_device(identifier: str) -> List:
        data = await Parser.ipsw(method="GET", endpoint=f"/keys/device/{identifier}")

        return [IPSWKeys(**keys) for keys in data]

    @staticmethod
    async def keys(identifier: str, buildid: str) -> IPSWKeys:
        data = await Parser.ipsw(
            method="GET", endpoint=f"/keys/ipsw/{identifier}/{buildid}"
        )
        data["keys"] = [KeysObject(**keys) for keys in data["keys"]]

        return IPSWKeys(**data)

    @staticmethod
    async def ota(identifier: str, buildid: str) -> OTAIPSW:
        data = await Parser.ipsw(method="GET", endpoint=f"/ota/{identifier}/{buildid}")

        return OTAIPSW(**data)

    @staticmethod
    async def ota_version(version: str) -> List:
        data = await Parser.ipsw(method="GET", endpoint=f"/ota/{version}")

        return [OTAIPSW(**ota) for ota in data]

    @staticmethod
    async def available_macos(seed: Optional[str] = "publicrelease"):
        return await SWSCAN.get_products(catalog_id=seed)

    @staticmethod
    async def get_macos(
        title: Optional[str] = None,
        buildid: Optional[str] = None,
        version: Optional[str] = None,
        product_id: Optional[str] = None,
        seed: Optional[str] = "publicseed",
    ) -> List:
        return await SWSCAN.get_package(
            title=title,
            build_id=buildid,
            version=version,
            product_id=product_id,
            catalog_id=seed,
        )


class Client(RealClient):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.loop = asyncio.get_event_loop()

    def __run_coroutine(self, coroutine, *args, **kwargs):
        if self.loop.is_running():
            return coroutine(*args, **kwargs)

        return self.loop.run_until_complete(coroutine(*args, **kwargs))

    def __getattribute__(self, name: str) -> Any:
        attribute = getattr(super(), name, None)

        if not attribute:
            return object.__getattribute__(self, name)

        if asyncio.iscoroutinefunction(attribute):
            return functools.partial(self.__run_coroutine, attribute)

        return attribute
