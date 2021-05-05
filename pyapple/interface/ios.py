from typing import Optional, Union

from hurry.filesize import alternative, size

from .base import BaseModel, to_dt


class IPSW(BaseModel):
    def __init__(
        self,
        identifier: str,
        buildid: str,
        version: str,
        url: str,
        filesize: int,
        sha1sum: str,
        md5sum: str,
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
        self.filesize = (filesize, size(filesize, system=alternative))
        self.sha1sum = sha1sum
        self.md5sum = md5sum
        self.signed = signed
        self.releasedate = to_dt(releasedate)
        self.uploaddate = to_dt(uploaddate)


class Keys(BaseModel):
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
        self.date = to_dt(date)


class IPSWKeys(BaseModel):
    def __init__(
        self,
        identifier: str,
        buildid: str,
        codename: str,
        baseband: Optional[str],
        updateramdiskexists: bool,
        restoreramdiskexists: bool,
        keys: Optional[list],
    ) -> None:
        self.identifier = identifier
        self.buildid = buildid
        self.codename = codename
        self.baseband = baseband
        self.updateramdiskexists = updateramdiskexists
        self.restoreramdiskexists = restoreramdiskexists
        self.keys = keys


class OTAIPSW(BaseModel):
    def __init__(
        self,
        identifier: str,
        buildid: str,
        version: str,
        url: str,
        filesize: int,
        prerequisitebuildid: str,
        prerequisiteversion: str,
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
        self.filesize = (filesize, size(filesize, system=alternative))
        self.prerequisitebuildid = prerequisitebuildid
        self.prerequisiteversion = prerequisiteversion
        self.release_type = release_type
        self.upload_date = to_dt(uploaddate)
        self.release_date = to_dt(releasedate)
        self.signed = signed


class iDevice(BaseModel):
    def __init__(
        self,
        name: str,
        identifier: str,
        boardconfig: str,
        platform: str,
        cpid: str,
        bdid: str,
        firmwares: Optional[list],
        boards: Optional[list],
    ) -> None:
        self.name = name
        self.identifier = identifier
        self.boardconfig = boardconfig
        self.platform = platform
        self.cpid = cpid
        self.bdid = bdid
        self.firmwares = firmwares
        self.boards = boards
