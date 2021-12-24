import asyncio
import functools
from typing import Any, Coroutine
from inspect import iscoroutinefunction

from .src import IPSWME, SHSH2, SWSCAN, Jailbreak, Pallas


class Client(IPSWME, SWSCAN, Jailbreak, SHSH2, Pallas):
    """
    Main class of PyApple.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    def sync(cls):
        client = cls()
        request_func = getattr(client, "request")

        async def session_closer(*args: Any, **kwargs: Any) -> Any:
            try:
                return await request_func(*args, **kwargs)

            finally:
                if client.session:
                    await client.session.close()

        def to_sync(func: Coroutine):
            def wrapper(*args: Any, **kwargs: Any):
                loop = asyncio.get_event_loop()

                if loop.is_running():
                    return func(*args, **kwargs)

                return loop.run_until_complete(func(*args, **kwargs))

            return wrapper

        setattr(client, "__aenter__", None)
        setattr(client, "__aexit__", None)
        setattr(client, "sync", None)

        del client.__aenter__
        del client.__aexit__
        del client.sync

        needs_to_be_changed = [
            fname
            for fname in dir(client)
            if iscoroutinefunction(getattr(client, fname))
        ]

        client.__setattr__("request", session_closer)

        for fname in needs_to_be_changed:
            client.__setattr__(fname, to_sync(getattr(client, fname)))

        return client
