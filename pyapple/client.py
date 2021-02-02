import asyncio
import functools
from typing import Any
from .swscan import SWSCAN
from .parser import Parser
from .model import iDevice, IPSW, IPSWKeys

IPSW_URL = "https://api.ipsw.me/v4"


class HALFTIME:
    def __init__(self) -> None:
        pass


class Client(HALFTIME):  # thanks to SaidbySolo (https://github.com/SaidBySolo/)
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