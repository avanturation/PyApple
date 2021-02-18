import asyncio
import functools
import json
from typing import Any, List

from .model import IPSW, OTAIPSW, IPSWKeys, iDevice
from .parser import Parser
from .swscan import SWSCAN

IPSW_URL = "https://api.ipsw.me/v4"


class HALFTIME:
    def __init__(self) -> None:
        self.SWSCAN = SWSCAN()

    async def device(self, identifier: str) -> iDevice:
        raw_data = Parser.request(f"{IPSW_URL}/device/{identifier}")
        data = json.loads(raw_data)

        firmware_list = []
        for pkg in data["firmwares"]:
            firmware_list.append(
                IPSW(
                    identifier=pkg["identifier"],
                    version=pkg["version"],
                    buildid=pkg["buildid"],
                    sha1=pkg["sha1sum"],
                    md5=pkg["md5sum"],
                    filesize=pkg["filesize"],
                    url=pkg["url"],
                    releasedate=pkg["releasedate"],
                    uploaddate=pkg["uploaddate"],
                    signed=pkg["signed"],
                )
            )

        return iDevice(
            name=data["name"],
            identifier=data["identifier"],
            boardconfig=data["boardconfig"],
            platform=data["platform"],
            cpid=data["cpid"],
            bdid=data["bdid"],
            firmwares=firmware_list,
        )

    async def ipsw(self, identifier: str, buildid: str) -> IPSW:
        raw_data = Parser.request(f"{IPSW_URL}/ipsw/{identifier}/{buildid}")
        data = json.loads(raw_data)

        return IPSW(
            identnfier=data["identifier"],
            version=data["version"],
            buildid=data["buildid"],
            url=data["url"],
            sha1=data["sha1sum"],
            md5=data["md5sum"],
            releasedate=data["releasedate"],
            uploaddate=data["uploaddate"],
            signed=data["signed"],
        )

    async def all_ipsw(self, version: str) -> List:
        raw_data = Parser.request(f"{IPSW_URL}/ipsw/{version}")
        data = json.loads(raw_data)
        firmware_list = []

        for firmware in data:
            ipsw_object = IPSW(
                identnfier=firmware["identifier"],
                version=firmware["version"],
                buildid=firmware["buildid"],
                url=firmware["url"],
                sha1=firmware["sha1sum"],
                md5=firmware["md5sum"],
                releasedate=firmware["releasedate"],
                uploaddate=firmware["uploaddate"],
                signed=firmware["signed"],
            )
            firmware_list.append(ipsw_object)

        return firmware_list

    async def all_keys_ipsw(self, identifier: str) -> List:
        raw_data = Parser.request(f"{IPSW_URL}/keys/device/{identifier}")
        data = json.loads(raw_data)
        keys_list = []

        for keys in data:
            key_object = IPSWKeys()


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
