import pprint
from datetime import date, datetime

from pyapple import Apple


async def sadf():
    d = datetime.now()
    apple = Apple()
    print(await apple.search_tweak(query="velvet"))
    t = datetime.now()
    print(t - d)


import asyncio

asyncio.run(sadf())
