import asyncio
import functools
import json
from typing import Any, Coroutine, List, Optional

from .model import IPSW, OTAIPSW, IPSWKeys, KeysObject, iDevice
from .parser import Parser
from .shsh2 import SHSH2
from .swscan import SWSCAN

IPSW_URL = "https://api.ipsw.me/v4"


class HALFTIME:
    def __init__(self) -> None:
        self.SWSCAN = SWSCAN()

    async def device(self, identifier: str) -> iDevice:
        raw_data = await Parser.request(f"{IPSW_URL}/device/{identifier}")
        data = json.loads(raw_data)

        firmware_list = []
        for pkg in data["firmwares"]:
            firmware_list.append(
                IPSW(
                    identifier=pkg["identifier"],
                    version=pkg["version"],
                    buildid=pkg["buildid"],
                    sha1=pkg["sha1sum"],
                    md5=pkg["md5sum"],
                    filesize=pkg["filesize"],
                    url=pkg["url"],
                    releasedate=pkg["releasedate"],
                    uploaddate=pkg["uploaddate"],
                    signed=pkg["signed"],
                )
            )

        return iDevice(
            name=data["name"],
            identifier=data["identifier"],
            boardconfig=data["boardconfig"],
            platform=data["platform"],
            cpid=data["cpid"],
            bdid=data["bdid"],
            firmwares=firmware_list,
        )

    async def ipsw(self, identifier: str, buildid: str) -> IPSW:
        raw_data = await Parser.request(f"{IPSW_URL}/ipsw/{identifier}/{buildid}")
        data = json.loads(raw_data)

        return IPSW(
            identifier=data["identifier"],
            version=data["version"],
            buildid=data["buildid"],
            url=data["url"],
            sha1=data["sha1sum"],
            md5=data["md5sum"],
            filesize=data["filesize"],
            releasedate=data["releasedate"],
            uploaddate=data["uploaddate"],
            signed=data["signed"],
        )

    async def all_ipsw(self, version: str) -> List:
        raw_data = await Parser.request(f"{IPSW_URL}/ipsw/{version}")
        data = json.loads(raw_data)
        firmware_list = []

        for firmware in data:
            ipsw_object = IPSW(
                identnfier=firmware["identifier"],
                version=firmware["version"],
                buildid=firmware["buildid"],
                url=firmware["url"],
                sha1=firmware["sha1sum"],
                md5=firmware["md5sum"],
                releasedate=firmware["releasedate"],
                uploaddate=firmware["uploaddate"],
                signed=firmware["signed"],
            )
            firmware_list.append(ipsw_object)

        return firmware_list

    async def all_keys_ipsw(self, identifier: str) -> List:
        raw_data = await Parser.request(f"{IPSW_URL}/keys/device/{identifier}")
        data = json.loads(raw_data)
        keys_list = []

        for keys in data:
            key_object = IPSWKeys(
                identifier=keys["identifier"],
                buildid=keys["buildid"],
                codename=keys["codename"],
                baseband=keys["baseband"],
                updateramdisk=keys["updateramdiskexists"],
                restoreramdisk=keys["restoreramdiskexists"],
            )
            keys_list.append(key_object)

        return keys_list

    async def keys_ipsw(self, identifier: str, buildid: str) -> IPSWKeys:
        raw_data = await Parser.request(f"{IPSW_URL}/keys/ipsw/{identifier}/{buildid}")
        data = json.loads(raw_data)
        real_key_list = []

        for keys in data["keys"]:
            object = KeysObject(
                image=keys["image"],
                filename=keys["filename"],
                kbag=keys["kbag"],
                key=keys["key"],
                iv=keys["iv"],
                date=keys["date"],
            )
            real_key_list.append(object)

        return IPSWKeys(
            identifier=data["identifier"],
            buildid=data["buildid"],
            codename=data["codename"],
            updateramdisk=data["updateramdiskexists"],
            restoreramdisk=data["restoreramdiskexists"],
            keys=real_key_list,
        )

    async def ota_ipsw(self, identifier: str, buildid: str) -> OTAIPSW:
        raw_data = await Parser.request(f"{IPSW_URL}/ota/{identifier}/{buildid}")
        data = json.loads(raw_data)

        return OTAIPSW(
            identifier=data["identifier"],
            buildid=data["buildid"],
            version=data["version"],
            url=data["url"],
            filesize=data["filesize"],
            prereq_buildid=data["prerequisitebuildid"],
            prereq_version=data["prerequisiteversion"],
            release_type=data["releasetype"],
            uploaddate=data["uploaddate"],
            releasedate=data["releasedate"],
            signed=data["signed"],
        )

    async def all_ota_ipsw(self, version: str) -> List:
        raw_data = await Parser.request(f"{IPSW_URL}/ota/{version}")
        data = json.loads(raw_data)
        all_ota_data = []

        for datas in data:
            obj = OTAIPSW(
                identifier=datas["identifier"],
                buildid=datas["buildid"],
                version=datas["version"],
                url=datas["url"],
                filesize=datas["filesize"],
                prereq_buildid=datas["prerequisitebuildid"],
                prereq_version=datas["prerequisiteversion"],
                release_type=datas["releasetype"],
                uploaddate=datas["uploaddate"],
                releasedate=datas["releasedate"],
                signed=datas["signed"],
            )
            all_ota_data.append(obj)

        return all_ota_data

    async def shsh2_blobs(
        self, ecid: str, model: str, version: str, apnonce: Optional[str]
    ) -> Coroutine:
        # Needs more touching
        shsh2_instance = SHSH2(ecid=ecid, apnonce=apnonce, model=model, version=version)

        return shsh2_instance.get_shsh2_blob()

    async def available_macos(self):
        list_macos = await self.SWSCAN.get_products()
        return list_macos

    async def get_macos(
        self, buildid: Optional[str], version: Optional[str], product_id: Optional[str]
    ) -> List:
        list_specific_macos = await self.SWSCAN.get_package(
            build_id=buildid, version=version, product_id=product_id
        )
        return list_specific_macos


class Client(HALFTIME):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.loop = asyncio.get_event_loop()

    def __run_coroutine(self, coroutine, *args, **kwargs):
        if self.loop.is_running():
            return coroutine(*args, **kwargs)

        return self.loop.run_until_complete(coroutine(*args, **kwargs))

    def __getattribute__(self, name: str) -> Any:
        attribute = getattr(super(), name, None)

        if not attribute:
            return object.__getattribute__(self, name)

        if asyncio.iscoroutinefunction(attribute):
            return functools.partial(self.__run_coroutine, attribute)

        return attribute
