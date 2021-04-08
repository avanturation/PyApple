from datetime import date, datetime
from pyapple import Client


async def sadf():
    c = Client()
    d = datetime.now()
    print(await c.available_macos())
    n = datetime.now()
    print(n - d)


import asyncio

asyncio.run(sadf())