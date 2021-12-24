import asyncio

from pyapple import Client

client = Client()

SUF = {"1": "publicrelease", "2": "publicbeta", "3": "developerbeta"}


async def fetch_all(catalog_id: str):
    result = await client.fetch_macos(catalog_id)

    print("Available macOS Products:")

    for macos in result:
        print(f"{macos.title} {macos.version} {macos.buildid}")


if __name__ == "__main__":
    print("1. Public Releases")
    print("2. Public Beta Releases")
    print("3. Developer Beta Releases")

    selection = input("Select: ")

    loop = asyncio.get_event_loop()
    loop.run_until_complete(fetch_all(SUF[selection]))
