import pprint
from datetime import date, datetime

from pyapple import Apple


async def sadf():
    apple = Apple()
    print(await apple.search_repo(slug="packix"))


import asyncio

asyncio.run(sadf())
