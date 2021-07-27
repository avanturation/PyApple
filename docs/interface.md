# PyApple Interfaces

This documents describes about dataclasses of PyApple.

## pyapple.interface.ios

### IPSW

Dataclass object of IPSW firmware.

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