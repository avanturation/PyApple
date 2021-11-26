"""
> Simple python library for dealing with Apple device's firmwares.

Example codes of this library are on the github repo.

Features:

    * Asynchronous (you can use synchronous method either)
    * Fetch IPSW by identifier, build number and version
    * Fetch OTA firmware by identifier, buildid and version
    * Fetch available MacOS from Apple's update server (including betas)
    * Get information of cydia tweak and repo
    * Extract SHSH2 blobs of iDevices
    * Request an asset from Apple's Pallas OTA server.


Github: https://github.com/fxrcha/PyApple
"""


from .client import Apple
from .src import Jailbreak, IPSWME, SHSH2, SWSCAN, Pallas
from .interface import *

__version__ = "2.0.0"

__all__ = [
    "Apple",
    "Jailbreak",
    "IPSWME",
    "SHSH2",
    "SWSCAN",
    "Pallas",
    "HTTPException",
    "NoCatalogResult",
    "IPSW",
    "OTA",
    "DeviceKeys",
    "FirmwareKeys",
    "iDevice",
    "MacOSProduct",
    "Package",
    "Repo",
    "Builds",
    "Tweak",
]
