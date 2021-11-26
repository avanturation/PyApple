# PyApple

> Simple python library for dealing with Apple device's firmwares.

## Features

* Asynchronous (you can use synchronous method either)
* Fetch IPSW by identifier, build number and version
* Fetch OTA firmware by identifier, buildid and version
* Fetch available MacOS from Apple's update server (including betas)
* Get information of cydia tweak and repo
* Extract SHSH2 blobs of iDevices
* Request an asset from Apple's Pallas OTA server.

## Example

```py
from pyapple import Apple

client = Apple()

device = client.search_device("iPad13,4")

print(device.name) # Prints "iPad Pro (11-inch) (3rd generation)"
```

You could see more example codes from [here](https://github.com/fxrcha/PyApple/main/example/README.md).

## Documentation

[here](https://github.com/fxrcha/PyApple/main/docs)

## Install

```zsh
python3 -m pip install pyapple
```

### Build Environment

* [macOS Monterey 12.0 beta 3 (21A5268h)](https://developer.apple.com/documentation/macos-release-notes/macos-12-beta-release-notes)
* [Python 3.9.4 64-bit](https://www.python.org/downloads/release/python-394/)
* [Mac mini (M1, 2020)](https://www.apple.com/mac-mini/) 

## Contribute

* Strongly recommends using black and isort.
* Use pull request.

## License

MIT License


