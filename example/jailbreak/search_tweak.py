import asyncio

from pyapple import Client

client = Client()


async def find_tweak(keyword: str):
    res = await client.search_tweak(query=keyword)
    res = res[0]

    print(f"Results for {keyword}")
    print(f"Name : {res.name}")
    print(f"ID : {res.package}")
    print(f"Description : {res.description}")
    print(f"Author : {res.author}")


if __name__ == "__main__":
    keyword = input("Search Tweak:")

    loop = asyncio.get_event_loop()
    loop.run_until_complete(find_tweak(keyword))
