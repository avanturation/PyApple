# PyApple

> Simple python library for dealing with Apple device's firmwares.

## Features

* Asynchronous
* Fetch IPSW by identifier, build number and version
* Fetch OTA firmware by identifier, buildid and version
* Fetch available MacOS from Apple's update server (including betas)
* Get information of cydia tweak and repo
* Extract SHSH2 blobs of iDevices
* Request an asset from Apple's Pallas OTA server.

## Example

```py
from asyncio import get_event_loop
from pyapple import Client

async def ipad():
    async with Client() as client:
        device = client.search_device("iPad13,4")
        print(device.name) # Prints "iPad Pro (11-inch) (3rd generation)"

get_event_loop().run_until_complete(ipad())
```

You could see more example codes from [here](https://github.com/fxrcha/PyApple/blob/main/example).

## Documentation

[here](https://github.com/fxrcha/PyApple/blob/main/docs)

## Install

```zsh
python3 -m pip install pyapple
```

## Contribute

* Strongly recommends using black and isort.
* Use pull request.

## License

MIT License


