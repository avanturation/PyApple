import aiohttp


class Parser:
    @staticmethod
    async def request(url: str, payload=None, header=None):
        async with aiohttp.ClientSession(headers=header) as session:
            async with session.get(url=url, params=payload) as r:
                data = await r.text()
        return data

    @staticmethod
    async def post(url: str, payload=None, header=None):
        async with aiohttp.ClientSession(headers=header) as session:
            async with session.post(url=url, params=payload) as r:
                data = await r.text()
        return data
