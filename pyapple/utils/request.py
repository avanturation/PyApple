import aiohttp

from .exceptions import HTTPException

SWSCAN_BASE = "https://swscan.apple.com/content/catalogs/others"
IPSW_BASE = "https://api.ipsw.me/v4"
CYDIA_BASE = " https://api.parcility.co/db"


class Parser:
    @staticmethod
    async def ipsw(method: str, endpoint: str):
        url = IPSW_BASE + endpoint
        async with aiohttp.ClientSession() as session:
            async with session.request(method, url) as resp:
                data = await resp.json(encoding="utf-8")

                if resp.status == 200:
                    return data

                raise HTTPException(resp.staus, url)

    @staticmethod
    async def cydia(endpoint: str):
        url = CYDIA_BASE + endpoint
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                data = await resp.json(encoding="utf-8")

                if data["status"] and data["code"] == 200:
                    return data

                raise HTTPException(data["code"], url)

    @staticmethod
    async def swscan(index: str, headers=None):
        url = SWSCAN_BASE + index
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(url) as resp:
                data = await resp.text()

                if resp.status == 200:
                    return data

                raise HTTPException(resp.staus, url)

    @staticmethod
    async def request(url: str):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                data = await resp.text()

                if resp.status == 200:
                    return data

                raise HTTPException(resp.staus, url)
