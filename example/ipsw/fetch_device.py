import asyncio

from pyapple import Apple

client = Apple()

# asynchronous
async def idevice_async(identiifer: str):
    device_data = await client.fetch_device(identiifer)

    print(f"Information of {device_data.name}")
    print(f"Identifier: {device_data.identifier}")
    print(f"Platform: {device_data.platform}")
    print(f"CPID: {device_data.cpid}")
    print(f"BDID: {device_data.bdid}")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(idevice_async("iPad13,4"))

# not asynchronous
def idevice(identiifer: str):
    device_data = client.fetch_device(identiifer)

    print(f"Information of {device_data.name}")
    print(f"Identifier: {device_data.identifier}")
    print(f"Platform: {device_data.platform}")
    print(f"CPID: {device_data.cpid}")
    print(f"BDID: {device_data.bdid}")


if __name__ == "__main__":
    idevice("iPad13,4")
