import dataclasses
from datetime import datetime
from typing import List, Optional

from dateutil import tz


def to_dt(time: Optional[str]):
    if time is None:
        return time  # early return

    dest = tz.tzutc()
    obj = datetime.strptime(time, "%Y-%m-%dT%H:%M:%SZ")
    obj = obj.replace(tzinfo=dest)
    return obj


@dataclasses.dataclass(init=True, repr=True)
class IPSW:
    __slots__ = (
        "identifier",
        "buildid",
        "version",
        "url",
        "filesize",
        "sha1sum",
        "md5sum",
        "releasedata",
        "uploaddate",
        "signed",
    )

    identifier: str
    buildid: str
    version: str
    url: str
    filesize: int
    sha1sum: str
    md5sum: str
    releasedate: Optional[str]
    uploaddate: Optional[str]
    signed: bool

    def __post_init__(self) -> None:
        self.releasedate = to_dt(self.releasedate)
        self.uploaddate = to_dt(self.uploaddate)


@dataclasses.dataclass(init=True, repr=True)
class FirmwareKeys:
    __slots__ = ("image", "filename", "kbag", "key", "iv", "date")

    image: str
    filename: str
    kbag: str
    key: str
    iv: str
    date: Optional[str]

    def __post_init__(self) -> None:
        self.date = to_dt(self.date)


@dataclasses.dataclass(init=True, repr=True)
class DeviceKeys:
    __slots__ = (
        "identifier",
        "buildid",
        "codename",
        "baseband",
        "updateramdiskexists",
        "restoreramdiskexists",
        "keys",
    )

    identifier: str
    buildid: str
    codename: str
    baseband: Optional[str]
    updateramdiskexists: bool
    restoreramdiskexists: bool
    keys: Optional[List]


@dataclasses.dataclass(init=True, repr=True)
class OTA:
    __slots__ = (
        "identifier",
        "buildid",
        "version",
        "url",
        "filesize",
        "prerequisitebuildid",
        "prerequisiteversion",
        "release_type",
        "uploaddate",
        "releasedate",
        "signed",
    )

    identifier: str
    buildid: str
    version: str
    url: str
    filesize: int
    prerequisitebuildid: str
    prerequisiteversion: str
    release_type: str
    uploaddate: Optional[str]
    releasedate: Optional[str]
    signed: bool

    def __post_init__(self) -> None:
        self.releasedate = to_dt(self.releasedate)
        self.uploaddate = to_dt(self.uploaddate)


@dataclasses.dataclass(init=True, repr=True)
class iDevice:
    __slots__ = (
        "name",
        "identifier",
        "boardconfig",
        "platform",
        "cpid",
        "bdid",
        "firmwares",
        "board",
    )

    name: str
    identifier: str
    boardconfig: str
    platform: str
    cpid: str
    bdid: str
    firmwares: Optional[List]
    boards: Optional[List]
