import pprint
from datetime import date, datetime

from pyapple import Apple


async def sadf():
    d = datetime.now()
    apple = Apple()
    print(apple.os_curdir())
    t = datetime.now()
    print(t - d)


import asyncio

asyncio.run(sadf())
