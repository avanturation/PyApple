import asyncio

from pyapple import Apple

client = Apple()


async def find_repo(keyword: str):
    res = await client.search_repo(slug=keyword)

    print(f"Results for {keyword}")
    print(f"Name : {res.label}")
    print(f"Codename : {res.codename}")
    print(f"Description : {res.description}")
    print(f"URL : {res.repo}")
    print(f"Numbers of package : {res.package_count}")


if __name__ == "__main__":
    keyword = input("Search Repo:")

    loop = asyncio.get_event_loop()
    loop.run_until_complete(find_repo(keyword))
