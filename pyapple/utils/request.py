from aiohttp import ClientSession

from ..interface import HTTPException

SWSCAN_BASE = "https://swscan.apple.com/content/catalogs/others"
IPSW_BASE = "https://api.ipsw.me/v4"
CYDIA_BASE = " https://api.parcility.co/db"


class AsyncRequest:
    @staticmethod
    async def ipsw(method: str, endpoint: str, **kwargs):
        url = IPSW_BASE + endpoint
        async with ClientSession() as session:
            async with session.request(method, url, params=kwargs) as resp:
                data = await resp.json(encoding="utf-8")

                if resp.status == 200:
                    return data

                raise HTTPException(resp.staus, url)

    @staticmethod
    async def cydia(endpoint: str, **kwargs):
        url = CYDIA_BASE + endpoint
        async with ClientSession() as session:
            async with session.get(url, params=kwargs) as resp:
                data = await resp.json(encoding="utf-8")

                if data["status"] and data["code"] == 200:
                    return data

                raise HTTPException(data["code"], url)

    @staticmethod
    async def swscan(index: str, headers=None, **kwargs):
        url = SWSCAN_BASE + index
        async with ClientSession(headers=headers) as session:
            async with session.get(url, params=kwargs) as resp:
                data = await resp.text()

                if resp.status == 200:
                    return data

                raise HTTPException(resp.staus, url)

    @staticmethod
    async def request(url: str, **kwargs):
        async with ClientSession() as session:
            async with session.get(url, params=kwargs) as resp:
                data = await resp.text()

                if resp.status == 200:
                    return data

                raise HTTPException(resp.staus, url)
