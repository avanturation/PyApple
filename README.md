# PyApple

> A Python wrapper for Apple firmwares (api.ipsw.me, swscan.apple.com)

## Features

* Check IPSW with iDevice identifier, and build id (including Apple Silicon Macs)

* Get information of OTA Packages

* Get all avaliable macOS (Intel-based)

* Download specific macOS (Intel-based)

## Example

```py
import pyapple

client = pyapple.Client()

ipsw = client.ipsw("iPhone12,1", "18B92")

print(ipsw.version) # Prints 14.2

print(ipsw.url) # Prints IPSW url (http://updates-http.cdn-apple.com/....)
```

## Install

```zsh
python3 -m pip install pyapple
```

### Build Environment

* [macOS Big Sur 11.1](https://www.apple.com/macos/big-sur/)

* [Python 3.8.6 for Darwin](https://www.python.org/downloads/release/python-386/)

* [MacBookPro15,1](https://support.apple.com/kb/SP776) and [Macmini9,1](https://www.apple.com/mac-mini/) (Tested on M1)

## Credits

[Apple](https://apple.com)

[ipsw.me](https://ipsw.me)



