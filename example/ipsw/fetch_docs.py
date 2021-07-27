import asyncio
import webbrowser
from pyapple import Apple

client = Apple()


async def ota_docs_async(identifier: str, version: str):
    document = await client.fetch_ota_docs(identifier, version)

    with open(f"{version}_{identifier}_docs.html", "w", encoding="utf-8") as f:
        f.write(document)

    webbrowser.open(f"file://{version}_{identifier}_docs.html", new=2)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(ota_docs_async("iPad13,4", "14.7"))


def ota_docs(identifier: str, version: str):
    document = client.fetch_ota_docs(identifier, version)

    with open(f"{version}_{identifier}_docs.html", "w", encoding="utf-8") as f:
        f.write(document)

    webbrowser.open(f"file://{version}_{identifier}_docs.html", new=2)


if __name__ == "__main__":
    ota_docs("iPad13,4", "14.7")
