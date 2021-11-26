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
    Dataclass object of IPSW firmware.
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
    """Identifier of target iDevice (e.g. iPhone12,1)"""
    buildid: str
    """Build string of IPSW firmware (e.g. 19A5297e)"""
    version: str
    """Version of IPSW firmware (e.g. 15.0)"""
    url: str
    """Download link of IPSW firmware"""
    filesize: int
    """Size of the IPSW firmware file"""
    sha1sum: str
    """SHA1 hash value of IPSW firmware file"""
    md5sum: str
    """MD5 value of IPSW firmware file"""
    releasedate: Optional[str]
    """Released date of IPSW firmware"""
    uploaddate: Optional[str]
    """Uploaded date of IPSW firmware"""
    signed: bool
    """Signing status of IPSW firmware. (*critical when downgrading or saving blobs)"""

    def __post_init__(self) -> None:
        self.releasedate = to_dt(self.releasedate)
        self.uploaddate = to_dt(self.uploaddate)


@dataclasses.dataclass(init=True, repr=True)
class FirmwareKeys:
    """
    Dataclass object of firmware decryption keys.
    """

    __slots__ = ("image", "filename", "kbag", "key", "iv", "date")

    image: str
    """Name of target image (e.g. GlyphCharging)"""
    filename: str
    """Full path of target image (e.g. Firmware/all_flash/all_fl ...)"""
    kbag: str
    """KBAG value of target image"""
    key: str
    """Key value of target image"""
    iv: str
    """IV value of target image"""
    date: Optional[str]
    """Created date of target image"""

    def __post_init__(self) -> None:
        self.date = to_dt(self.date)


@dataclasses.dataclass(init=True, repr=True)
class DeviceKeys:
    """
    Dataclass object of device keys.
    """

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
    """Identifier of target iDevice (e.g. iPhone12,1)"""
    buildid: str
    """Build string of IPSW firmware (e.g. 19A5297e)"""
    codename: str
    """Codename of firmware"""
    baseband: Optional[str]
    """Baseband date of target iDevice"""
    updateramdiskexists: bool
    """Existence of update ramdisk"""
    restoreramdiskexists: bool
    """Existence of restore ramdisk"""
    keys: Optional[List]
    """"""


@dataclasses.dataclass(init=True, repr=True)
class OTA:
    """
    Dataclass object of OTA firmware.
    """

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
    """Identifier of target iDevice."""
    buildid: str
    """Build string of OTA firmware."""
    version: str
    """iOS/iPadOS version of OTA firmware."""
    url: str
    """Download link of OTA firmware"""
    filesize: int
    """Size of OTA firmware."""
    prerequisitebuildid: str
    """Required build to update from."""
    prerequisiteversion: str
    """Required iOS/iPadOS version to update from."""
    release_type: str
    """Release type of OTA firmware."""
    uploaddate: Optional[str]
    """Uploaded date of OTA firmware."""
    releasedate: Optional[str]
    """Released date of OTA firmware."""
    signed: bool
    """Signing status of OTA firmware."""

    def __post_init__(self) -> None:
        self.releasedate = to_dt(self.releasedate)
        self.uploaddate = to_dt(self.uploaddate)


@dataclasses.dataclass(init=True, repr=True)
class iDevice:
    """
    Dataclass object of iDevice.
    """

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
    """Name of iDevice."""
    identifier: str
    """Identifier of iDevice."""
    boardconfig: str
    """Boardconfig of iDevice."""
    platform: str
    """AP codename (or platform) of iDevice."""
    cpid: str
    """CPID of iDevice."""
    bdid: str
    """BDID of iDevice."""
    firmwares: Optional[List]
    """List of all available IPSW firmwares of iDevice."""
    boards: Optional[List]
    """All available boardconfigs of iDevice."""
