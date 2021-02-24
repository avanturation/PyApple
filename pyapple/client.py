import asyncio
import functools
from typing import Any, List, Optional

from .model import IPSW, OTAIPSW, IPSWKeys, KeysObject, iDevice
from .parser import Parser
from .swscan import SWSCAN

IPSW_URL = "https://api.ipsw.me/v4"


class HALFTIME:
    def __init__(self) -> None:
        self.SWSCAN = SWSCAN()

    async def device(self, identifier: str) -> iDevice:
        data = await Parser.ipsw(method="GET", endpoint=f"/device/{identifier}")
        firmware_list = []

        for pkg in data["firmwares"]:
            firmware_list.append(IPSW(**pkg))

        data["firmwares"] = firmware_list

        return iDevice(**data)

    async def ipsw(self, identifier: str, buildid: str) -> IPSW:
        data = await Parser.ipsw(method="GET", endpoint=f"/ipsw/{identifier}/{buildid}")

        return IPSW(**data)

    async def ipsw_version(self, version: str) -> List:
        data = await Parser.ipsw(method="GET", endpoint=f"/ipsw/{version}")
        firmware_list = []

        for firmware in data:
            ipsw_object = IPSW(**firmware)
            firmware_list.append(ipsw_object)

        return firmware_list

    async def keys_device(self, identifier: str) -> List:
        data = await Parser.ipsw(method="GET", endpoint=f"/keys/device/{identifier}")
        keys_list = []

        for keys in data:
            key_object = IPSWKeys(**keys)
            keys_list.append(key_object)

        return keys_list

    async def keys(self, identifier: str, buildid: str) -> IPSWKeys:
        data = await Parser.ipsw(
            method="GET", endpoint=f"/keys/ipsw/{identifier}/{buildid}"
        )
        key_list = []

        for keys in data["keys"]:
            object = KeysObject(**keys)
            key_list.append(object)

        data["keys"] = key_list

        return IPSWKeys(**data)

    async def ota(self, identifier: str, buildid: str) -> OTAIPSW:
        data = await Parser.ipsw(method="GET", endpoint=f"/ota/{identifier}/{buildid}")

        return OTAIPSW(**data)

    async def ota_version(self, version: str) -> List:
        data = await Parser.ipsw(method="GET", endpoint=f"/ota/{version}")
        ota_data = []

        for otas in data:
            obj = OTAIPSW(**otas)
            ota_data.append(obj)

        return ota_data

    async def available_macos(self, seed: Optional[str] = "publicseed"):
        list_macos = await self.SWSCAN.get_products(catalog_id=seed)
        return list_macos

    async def get_macos(
        self,
        buildid: Optional[str],
        version: Optional[str],
        product_id: Optional[str],
        seed: Optional[str] = "publicseed",
    ) -> List:
        list_specific_macos = await self.SWSCAN.get_package(
            build_id=buildid, version=version, product_id=product_id, catalog_id=seed
        )
        return list_specific_macos


class Client(HALFTIME):
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
