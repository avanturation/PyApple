import asyncio
import aiohttp
from tqdm import tqdm

from pyapple import Client

client = Client()


async def download(url: str, name: str, buildid: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            with tqdm(
                total=int(resp.headers["content-length"], 0),
                unit="",
                desc=f"Downloading {name}: ",
                unit_divisor=1024,
                ascii=True,
                unit_scale=True,
            ) as bar:
                with open(f"{buildid}/{name}", "wb") as f:
                    async for chunk in resp.content.iter_chunked(1024):
                        f.write(chunk)
                        bar.update(len(chunk))


async def download_monterey():
    monterey_result = await client.search_macos(
        version="12", catalog_id="developerbeta"
    )

    real_monterey = monterey_result[0]
    print("Latest macOS Moneterey build details:")
    print(f"Title: {real_monterey.title}")
    print(f"Version: {real_monterey.version}")
    print(f"Build ID: {real_monterey.buildid}")
    print(f"Uploaded date: {real_monterey.postdate}")

    print("Starting download")
    for package in real_monterey.packages:
        await download(package.url, package.filename, real_monterey.buildid)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(download_monterey())
