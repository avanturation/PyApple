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


@dataclasses.dataclass(repr=True)
class IPSW:
    """
    Dataclass of IPSW firmware.

    Arguments:
        `identifier` (str) - Identifier of target iDevice (e.g. iPhone12,1)
        `buildid` (str) - Build string of IPSW firmware (e.g. 19A5297e)
        `version` (str) - Version of IPSW firmware (e.g. 15.0)
        `url` (str) - Download link of IPSW firmware
        `filesize` (int) - Size of the IPSW firmware file
        `sha1sum` (str) - SHA1 hash value of IPSW firmware file
        `md5sum` (str) - MD5 value of IPSW firmware file
        `releasedate` (datetime.datetime) - Released date of IPSW firmware
        `uploaddate` (datetime.datetime) - Uploaded date of IPSW firmware
        `signed` (bool) - Signing status of IPSW firmware. (*critical when downgrading or saving blobs)
    """

    __slots__ = (
        "identifier",
        "buildid",
        "version",
        "url",
        "filesize",
        "sha1sum",
        "md5sum",
        "releasedate",
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
    """
    Dataclass of firmware decryption keys.

    Arguments:
        `image` (str) - Name of target image (e.g. GlyphCharging)
        `filename` (str) - Full path of target image (e.g. Firmware/all_flash/all_fl ...)
        `kbag` (str) - KBAG value of target image
        `key` (str) - Key value of target image
        `iv` (str) - IV value of target image
        `date` (datetime.datetime) - Created date of target image
    """

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
        "boards",
    )

    name: str
    identifier: str
    boardconfig: str
    platform: str
    cpid: str
    bdid: str
    firmwares: Optional[List]
    boards: Optional[List]
