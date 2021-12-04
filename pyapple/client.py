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
