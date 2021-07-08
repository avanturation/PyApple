from datetime import date, datetime
from pyapple import Apple
import pprint


async def sadf():
    apple = Apple()
    pprint.pprint(
        await apple.get_package(
            title="macOS",
            version="12.0",
            build_id=None,
            catalog_id="developerbeta",
        )
    )


import asyncio

asyncio.run(sadf())
