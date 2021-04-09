from datetime import date, datetime
from pyapple import Client


async def sadf():
    d = datetime.now()
    print(await Client.available_macos())
    n = datetime.now()
    print(n - d)


import asyncio

asyncio.run(sadf())