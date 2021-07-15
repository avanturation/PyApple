# PyApple

> iDevice utility library written in Python

## Features

* Asynchronous (you can use synchronous method either)

* Fetch IPSW by identifier, buildid and version

* Fetch OTA firmware by identifier, buildid and version

* Fetch available MacOS from Apple server (including betas)

* Get information of cydia tweak and repo

* Extract SHSH2 blobs of iDevices

## Example

```py
from pyapple import Apple

client = Apple()

device = client.search_device("iPad13,4")

print(device.name) # Prints "iPad Pro (11-inch) (3rd generation)"
```

## Install

```zsh
python3 -m pip install pyapple
```

### Build Environment

* [macOS Monterey 12.0 beta 3 (21A5268h)](https://developer.apple.com/documentation/macos-release-notes/macos-12-beta-release-notes)

* [Python 3.9.4 64-bit](https://www.python.org/downloads/release/python-394/)

* [Mac mini (M1, 2020)](https://www.apple.com/mac-mini/) 

## Used technologies

[Apple](https://apple.com)

[ipsw.me](https://ipsw.me)

[Parcility](https://developers.parcility.co/docs#get-dbsearch)



