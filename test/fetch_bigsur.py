from datetime import date, datetime
from pyapple import Client

import pprint


async def sadf():
    pprint.pprint(
        await Client.get_macos(
            title="macOS Big Sur",
            version="11.3.1",
            buildid=None,
            product_id=None,
            seed="publicrelease",
        )
    )


import asyncio

asyncio.run(sadf())
