from datetime import date, datetime
from pyapple import Apple
import pprint


async def sadf():
    apple = Apple()
    await apple.ota_docs("iPhone", "14.6")


import asyncio

asyncio.run(sadf())
