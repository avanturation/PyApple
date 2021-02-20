from datetime import datetime
from typing import Optional, Union

from dateutil import tz
from hurry.filesize import alternative, size


class IPSW:
    """
    A Python class for Regular IPSW files.

    Arguments:
    identifier: iDevice identifier for IPSW
    buildid: Build ID of IPSW
    version: OS Version of IPSW
    url: Download link of IPSW
    filesize: Size of IPSW file (in integer)
    sha1: SHA1 sum of IPSW file
    md5: MD5 sum of IPSW file
    releasedate: Released date of IPSW (in string)
    uploaddate: Uploaded date of IPSW (in string)
    signed: A bool whether tells IPSW is still signed
    """

    def __init__(
        self,
        identifier: str,
        buildid: str,
        version: str,
        url: str,
        filesize: int,
        sha1: str,
        md5: str,
        releasedate: Union[
            str, None
        ],  # sometimes Apple gives firmware release date as null, fuck
        uploaddate: Union[
            str, None
        ],  # sometimes Apple gives firmware release date as null, fuck
        signed: bool,
    ) -> None:
        self.identifier = identifier
        self.buildid = buildid
        self.version = version
        self.uri = url
        self.filesize = (filesize, self._tofilesize(filesize))
        self.sha1 = sha1
        self.md5 = md5
        self.signed = signed
        self.releasedate = self._todatetime(releasedate)
        self.uploaddate = self._todatetime(uploaddate)

    def _todatetime(self, time: Union[str, None]):
        if time is not None:
            dest = tz.tzutc()
            obj = datetime.strptime(time, "%Y-%m-%dT%H:%M:%SZ")
            obj = obj.replace(tzinfo=dest)
            return obj
        else:
            return time

    def _tofilesize(self, value: int):
        return size(value, system=alternative)


class KeysObject:
    def __init__(
        self,
        image: str,
        filename: str,
        kbag: str,
        key: str,
        iv: str,
        date: Optional[str],
    ) -> None:
        self.image = image
        self.filename = filename
        self.kbag = kbag
        self.key = key
        self.iv = iv
        self.date = self._todatetime(date)

    def _todatetime(self, time: Union[str, None]):
        if time is not None:
            dest = tz.tzutc()
            obj = datetime.strptime(time, "%Y-%m-%dT%H:%M:%SZ")
            obj = obj.replace(tzinfo=dest)
            return obj
        else:
            return time


class IPSWKeys:
    def __init__(
        self,
        identifier: str,
        buildid: str,
        codename: str,
        baseband: Optional[str],
        updateramdisk: bool,
        restoreramdisk: bool,
        keys: Optional[list],
    ) -> None:
        self.identifier = identifier
        self.buildid = buildid
        self.codename = codename
        self.baseband = baseband
        self.updateramdisk = updateramdisk
        self.restoreramdisk = restoreramdisk
        self.keys = keys


class OTAIPSW:
    def __init__(
        self,
        identifier: str,
        buildid: str,
        version: str,
        url: str,
        filesize: int,
        prereq_buildid: str,
        prereq_version: str,
        release_type: str,
        uploaddate: Union[
            str, None
        ],  # sometimes Apple gives firmware release date as null, fuck
        releasedate: Union[
            str, None
        ],  # sometimes Apple gives firmware release date as null, fuck
        signed: bool,
    ) -> None:
        self.identifier = identifier
        self.buildid = buildid
        self.version = version
        self.uri = url
        self.filesize = (filesize, self._tofilesize(filesize))
        self.prereq_buildid = prereq_buildid
        self.prereq_version = prereq_version
        self.release_type = release_type
        self.upload_date = self._todatetime(uploaddate)
        self.release_date = self._todatetime(releasedate)
        self.signed = signed

    def _todatetime(self, time: Union[str, None]):
        if time is not None:
            dest = tz.tzutc()
            obj = datetime.strptime(time, "%Y-%m-%dT%H:%M:%SZ")
            obj = obj.replace(tzinfo=dest)
            return obj
        else:
            return time

    def _tofilesize(self, value: int):
        return size(value, system=alternative)


class iDevice:
    """
    A Python class for an iDevice.

    Arguments:
    name: Name of iDevice
    identifier: Identifier of iDevice
    boardconfig: Boardconfig of iDevice
    platform: CPU Platform of iDevice
    cpid: CPID of iDevice
    bdid: BDID of iDevice
    firmwares: List of available firmwares of iDevice
    """

    def __init__(
        self,
        name: str,
        identifier: str,
        boardconfig: str,
        platform: str,
        cpid: str,
        bdid: str,
        firmwares: Optional[list],
    ) -> None:
        self.name = name
        self.identifier = identifier
        self.boardconfig = boardconfig
        self.platform = platform
        self.cpid = cpid
        self.bdid = bdid
        self.firmwares = firmwares


class IntelMacOS:
    """
    A Python class for an Intel-based macOS Installation.

    Arguments:
    product_id: A product id of macOS Installation
    title: A title of macOS Installation
    version: Version of macOS
    build: Build ID of macOS
    packages: List of macOS Packages
    """

    def __init__(self, product_id) -> None:
        self.product_id = product_id
        self.title = ""
        self.version = ""
        self.build = ""
        self.packages = []


class IntelMacOSPkg:
    def __init__(self, url: str, filesize: int) -> None:
        self.filename = self._getname(url)
        self.uri = url
        self.filesize = (filesize, self._tofilesize(filesize))

    def _getname(self, uri):
        return uri.split("/")[-1]

    def _tofilesize(self, value: int):
        return size(value, system=alternative)
