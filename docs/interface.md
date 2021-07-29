# PyApple Interfaces

This document describes about dataclasses of PyApple.

## pyapple.interface.ios

### IPSW

**Dataclass object of IPSW firmware.**

Attributes:
| Variable    | Type              | Description                           |
|-------------|-------------------|---------------------------------------|
| identifier  | str               | Identifier of target iDevice          |
| buildid     | str               | Build string of IPSW firmware         |
| version     | str               | Version of IPSW firmware              |
| url         | str               | Download link of IPSW firmware        |
| filesize    | int               | Size of the IPSW firmware file        |
| sha1sum     | str               | SHA1 hash value of IPSW firmware file |
| md5sum      | str               | MD5 value of IPSW firmware file       |
| releasedate | datetime.datetime | Released date of IPSW firmware        |
| uploaddate  | datetime.datetime | Uploaded date of IPSW firmware        |
| signed      | bool              | Signing status of IPSW firmware       |

### FirmwareKeys

**Dataclass object of firmware decryption keys.**

Attributes:
| Variable | Type               | Description                  |
|----------|--------------------|------------------------------|
| image    | str                | Name of target image         |
| filename | str                | Full path of target image    |
| kbag     | str                | KBAG value of target image   |
| key      | str                | Key value of target image    |
| iv       | str                | IV value of target image     |
| date     | datetime.datetime  | Created date of target image |

### DeviceKeys

**Dataclass object of device keys.**

Attributes:
| Variable             | Type | Description                     |
|----------------------|------|---------------------------------|
| identifier           | str  | Identifier of target iDevice    |
| buildid              | str  | Build string of IPSW firmware   |
| codename             | str  | Codename of firmware            |
| baseband             | str  | Baseband date of target iDevice |
| updateramdiskexists  | bool | Existence of update ramdisk     |
| restoreramdiskexists | bool | Existence of restore ramdisk    |

### OTA

**Dataclass object of OTA firmware.**

Attributes:
| Variable            | Type              | Description                     |
|---------------------|-------------------|---------------------------------|
| identifier          | str               | Identifier of target iDevice    |
| buildid             | str               | Build string of OTA firmware    |
| version             | str               | Version of OTA firmware         |
| url                 | str               | Download link of OTA firmware   |
| filesize            | int               | Size of the OTA firmware file   |
| prerequisitebuildid | str               | Required build to update from   |
| prerequisiteversion | str               | Required version to update from |
| release_type        | str               | Release type of OTA firmware    |
| releasedate         | datetime.datetime | Released date of OTA firmware   |
| uploaddate          | datetime.datetime | Uploaded date of OTA firmware   |
| signed              | bool              | Signing status of OTA firmware  |

### OTA

**Dataclass object of iDevice.**

Attributes:
| Variable    | Type       | Description                                     |
|-------------|------------|-------------------------------------------------|
| name        | str        | Name of iDevice                                 |
| identifier  | str        | Identifier of iDevice                           |
| boardconfig | str        | Boardconfig of iDevice                          |
| platform    | str        | AP codename (or platform) of iDevice            |
| cpid        | int        | CPID of iDevice                                 |
| bdid        | str        | BDID of iDevice                                 |
| firmwares   | List(IPSW) | List of all available IPSW firmwares of iDevice |
| boards      | list       | All available boardconfigs of iDevice           |


## pyapple.interface.macos

### MacOSProduct

**Dataclass object of a single macOS product.**

Attributes:
| Variable   | Type               | Description                           |
|------------|--------------------|---------------------------------------|
| product_id | str                | Product ID of the macOS product       |
| title      | str                | Title of the macOS product            |
| version    | str                | macOS version of the product          |
| buildid    | str                | Build string of the macOS product     |
| postdate   | datetime.datetime  | Posted date of the macOS product      |
| packages   | List(Package)      | List of packages of the macOS product |

### Package

**Dataclass object of product package.**

Attributes:
| Variable | Type | Description                  |
|----------|------|------------------------------|
| url      | str  | URL link of the package file |
| filename | str  | Filename of the package file |
| filesize | str  | Size of the package file     |