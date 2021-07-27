import asyncio

from pyapple import Apple

client = Apple()

if __name__ == "__main__":
    print("Saving your iPhone's blob.")

    loop = asyncio.get_event_loop()
    loop.run_until_complete(
        client.latest_blobs(
            "iPhone12,1", ecid="secret", apnonce="secret", generator="secret"
        )
    )
