import orjson
import asyncio
import functools
from typing import Any
from .swscan import SWSCAN
from .parser import Parser
from .model import iDevice, IPSW, IPSWKeys, OTAIPSW

IPSW_URL = "https://api.ipsw.me/v4"


class HALFTIME:
    def __init__(self) -> None:
        pass

    async def device(self, identifier: str) -> iDevice:
        raw_data = Parser.request(f"{IPSW_URL}/device/{identifier}")
        data = orjson.loads(raw_data)

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