import pprint
from datetime import date, datetime

from pyapple import Apple


async def sadf():
    d = datetime.now()

    t = datetime.now()
    print(t - d)


apple = Apple()
apple.fetch_device("iPhone12,1")
