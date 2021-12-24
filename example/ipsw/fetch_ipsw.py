import asyncio

from pyapple import Client

client = Client()


# asynchronous way
async def fetch_firmwares_async(version: str):
    firmware_data = await client.fetch_ipsw_version(version)
    print(f"There are {len(firmware_data)} firmwares for iOS {version}.")

    available_devices = [ipsw.identifier for ipsw in firmware_data]

    print("Available devices: ")
    print(", ".join(available_devices[:]))


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(fetch_firmwares_async("14.7"))


# not asynchronous
def fetch_firmwares(version: str):
    client = Client.sync()
    firmware_data = client.fetch_ipsw_version(version)
    print(f"There are {len(firmware_data)} firmwares for iOS {version}.")

    available_devices = [ipsw.identifier for ipsw in firmware_data]

    print("Available devices: ")
    print(", ".join(available_devices[:]))


if __name__ == "__main__":
    fetch_firmwares("14.7")
