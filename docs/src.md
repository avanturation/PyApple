# PyApple Classes

This document describes about main classes of PyApple.

## pyapple.src.ipsw.IPSWME

### fetch_device

**Fetches iDevice from ipsw.me API.**

Args:

    identifier (str): Identifier of iDevice. (e.g. iPhone12,1)

Returns:

    iDevice: Dataclass object of iDevice.

### search_ipsw

**Searches specfic IPSW firmware from ipsw.me API.**

Args:

    identifier (str): Identifier of iDevice. (e.g. iPhone12,1)
    buildid (str): Build ID of IPSW firmware. (e.g. 19A5297e)

Returns:

    IPSW: Dataclass object of IPSW firmware.

### fetch_ipsw_version

**Fetches all iOS/iPadOS firmware by version from ipsw.me API.**

Args:

    version (str): iOS/iPadOS version to search. (e.g. 14.7)

Returns:

    List[IPSW]: List of searched IPSW dataclass objects.

### device_keys

**Searches key data of iDevice from ipsw.me API**

Args:

    version (str): iOS/iPadOS version to search. (e.g. 14.7)

Returns:

    List[DeviceKeys]: List of device keys dataclass objects.

### firmware_keys

**Searches key data of IPSW firmware from ipsw.me API.**

Args:

    identifier (str): Identifier of iDevice. (e.g. iPhone12,1)
    buildid (str): Build ID of IPSW firmware. (e.g. 19A5297e)

Returns:

    DeviceKeys: Dataclass object of device and firmware keys.

### search_ota

**Searches OTA firmware by identifier and buildid from ipsw.me API.**

Args:

    identifier (str): Identifier of iDevice. (e.g. iPhone12,1)
    buildid (str): Build ID of IPSW firmware. (e.g. 19A5297e)

Returns:

    OTA: Dataclass object of OTA firmware.

### fetch_ota_version

**Fetches OTA firmware by iOS/iPadOS version from ipsw.me API.**

Args:

    version (str): iOS/iPadOS version to search. (e.g. 14.7)

Returns:

    List[OTA]: List of OTA firmwares.

### fetch_ota_docs

**Fetches OTA documentation by identifier and iOS/iPadOS version from ipsw.me API.**

Args:

    identifier (str): Identifier of iDevice. (e.g. iPhone12,1)
    version (str): iOS/iPadOS version to search. (e.g. 14.7)

Returns:

    str: String of OTA documentation.
