from typing import List

from ..interface import IPSW, OTA, DeviceKeys, FirmwareKeys, iDevice
from ..utils import AsyncRequest


class IPSWME:
    """Class for ipsw.me related functions."""

    def __init__(self) -> None:
        self.__HTTP = AsyncRequest()
        super().__init__()

    async def fetch_device(self, identifier: str) -> iDevice:
        """Fetches iDevice from ipsw.me API.

        Args:
            identifier (str): Identifier of iDevice. (e.g. iPhone12,1)

        Returns:
            iDevice: Dataclass object of iDevice.
        """

        data = await self.__HTTP.ipsw(
            endpoint=f"/device/{identifier}", return_type="json"
        )
        data["firmwares"] = [IPSW(**firmware) for firmware in data["firmwares"]]

        await self.__HTTP.session.close()
        return iDevice(**data)

    async def search_ipsw(self, identifier: str, buildid: str) -> IPSW:
        """Searches specfic IPSW firmware from ipsw.me API.

        Args:
            identifier (str): Identifier of iDevice. (e.g. iPhone12,1)
            buildid (str): Build ID of IPSW firmware. (e.g. 19A5297e)

        Returns:
            IPSW: Dataclass object of IPSW firmware.
        """
        data = await self.__HTTP.ipsw(
            endpoint=f"/ipsw/{identifier}/{buildid}", return_type="json"
        )

        await self.__HTTP.session.close()
        return IPSW(**data)

    async def fetch_ipsw_version(self, version: str) -> List[IPSW]:
        """Fetches all iOS/iPadOS firmware by version from ipsw.me API.

        Args:
            version (str): iOS/iPadOS version to search. (e.g. 14.7)

        Returns:
            List[IPSW]: List of searched IPSW dataclass objects.
        """
        data = await self.__HTTP.ipsw(endpoint=f"/ipsw/{version}", return_type="json")

        await self.__HTTP.session.close()
        return [IPSW(**firmware) for firmware in data]

    async def device_keys(self, identifier: str) -> List[DeviceKeys]:
        """Searches key data of iDevice from ipsw.me API.

        Args:
            identifier (str): Identifier of iDevice. (e.g. iPhone12,1)

        Returns:
            List[DeviceKeys]: List of device keys dataclass objects.
        """
        data = await self.__HTTP.ipsw(
            endpoint=f"/keys/device/{identifier}", return_type="json"
        )

        await self.__HTTP.session.close()
        return [DeviceKeys(**keys) for keys in data]

    async def firmware_keys(self, identifier: str, buildid: str) -> DeviceKeys:
        """Searches key data of IPSW firmware from ipsw.me API.

        Args:
            identifier (str): Identifier of iDevice. (e.g. iPhone12,1)
            buildid (str): Build ID of IPSW firmware. (e.g. 19A5297e)

        Returns:
            DeviceKeys: Dataclass object of device and firmware keys.
        """
        data = await self.__HTTP.ipsw(
            endpoint=f"/keys/ipsw/{identifier}/{buildid}", return_type="json"
        )
        data["keys"] = [FirmwareKeys(**keys) for keys in data["keys"]]

        await self.__HTTP.session.close()
        return DeviceKeys(**data)

    async def search_ota(self, identifier: str, buildid: str) -> OTA:
        """Searches OTA firmware by identifier and buildid from ipsw.me API.

        Args:
            identifier (str): Identifier of iDevice. (e.g. iPhone12,1)
            buildid (str): Build ID of IPSW firmware. (e.g. 19A5297e)

        Returns:
            OTA: Dataclass object of OTA firmware.
        """
        data = await self.__HTTP.ipsw(
            endpoint=f"/ota/{identifier}/{buildid}", return_type="json"
        )

        await self.__HTTP.session.close()
        return OTA(**data)

    async def fetch_ota_version(self, version: str) -> List[OTA]:
        """Fetches OTA firmware by iOS/iPadOS version from ipsw.me API.

        Args:
            version (str): iOS/iPadOS version to search. (e.g. 14.7)

        Returns:
            List[OTA]: List of OTA firmwares.
        """
        data = await self.__HTTP.ipsw(endpoint=f"/ota/{version}", return_type="json")

        await self.__HTTP.session.close()
        return [OTA(**ota) for ota in data]

    async def fetch_ota_docs(self, identifier: str, version: str) -> str:
        """Fetches OTA documentation by identifier and iOS/iPadOS version from ipsw.me API.

        Args:
            identifier (str): Identifier of iDevice. (e.g. iPhone12,1)
            version (str): iOS/iPadOS version to search. (e.g. 14.7)

        Returns:
            str: String of OTA documentation.
        """
        data = await self.__HTTP.ipsw(
            endpoint=f"/ota/documentation/{identifier}/{version}", return_type="text"
        )

        await self.__HTTP.session.close()
        return data
