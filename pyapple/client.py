import asyncio
import functools
from typing import Any

from .src import IPSWME, SHSH2, SWSCAN, Jailbreak


class Apple(IPSWME, SWSCAN, Jailbreak, SHSH2):
    """
    Main class of PyApple.

    Inherited classes:
        `pyapple.src.ipsw.IPSWME` - ipsw.me related class.
        `pyapple.src.swscan.SWSCAN` - swscan.apple.com related class.
        `pyapple.src.shsh2.SHSH2` - SHSH2 related class.
        `pyapple.src.jaibreak.Jailbreak` - Jailbreak related class.
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
