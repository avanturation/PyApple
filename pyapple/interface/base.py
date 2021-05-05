from datetime import datetime
from typing import Optional

from dateutil import tz


class BaseModel:
    def __repr__(self) -> str:
        return str(self.__dict__)

    def __str__(self) -> str:
        return str(self.__dict__)


def to_dt(time: Optional[str]):
    if time is None:
        return time  # early return

    dest = tz.tzutc()
    obj = datetime.strptime(time, "%Y-%m-%dT%H:%M:%SZ")
    obj = obj.replace(tzinfo=dest)
    return obj
