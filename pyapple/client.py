import asyncio
import functools
from typing import Any

from .src import IPSWME, SHSH2, SWSCAN, Jailbreak, Pallas


class Apple(IPSWME, SWSCAN, Jailbreak, SHSH2, Pallas):
    """
    Main class of PyApple.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.loop = asyncio.get_event_loop()

    def __run_coroutine(self, coroutine, *args, **kwargs):
        if self.loop.is_running():
            return coroutine(*args, **kwargs)

        return self.loop.run_until_complete(coroutine(*args, **kwargs))

    def __getattribute__(self, name: str):
        attribute = getattr(super(), name, None)

        if not attribute:
            return object.__getattribute__(self, name)

        if asyncio.iscoroutinefunction(attribute):
            return functools.partial(self.__run_coroutine, attribute)

        return attribute
