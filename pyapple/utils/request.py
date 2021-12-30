from typing import Any, Optional

from aiohttp import ClientSession

from ..interface import HTTPException

from plistlib import loads

SWSCAN_BASE = ""
IPSW_BASE = "https://api.ipsw.me/v4"
PARCILITY_BASE = "https://api.parcility.co"


class Base:
    def __init__(self) -> None:
        self.session: Optional[ClientSession] = None

    async def request(
        self,
        url: str,
        method: str,
        return_type: str,
        **kwargs: Any,
    ):
        if not self.session or self.session.closed:
            self.session = ClientSession()

        resp = await self.session.request(method, url, **kwargs)

        if resp.status == 200:
            return await getattr(resp, return_type)()

        else:
            raise HTTPException(resp.status, url)

    async def post(self, url: str, **kwargs: Any):
        return await self.request(url, "POST", **kwargs)

    async def get(self, url: str, **kwargs: Any):
        return await self.request(url, "GET", **kwargs)

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        if self.session:
            await self.session.close()


class Requester(Base):
    async def ipsw(self, endpoint: str, **kwargs):
        url = IPSW_BASE + endpoint
        return await self.get(url, **kwargs)

    async def parcility(self, endpoint: str, **kwargs):
        url = PARCILITY_BASE + endpoint
        data = await self.get(url, return_type="json", **kwargs)

        if data["status"] and data["code"] == 200:
            return data["data"]

        raise HTTPException(data["code"], url)

    async def swscan(self, index: str, headers=None, **kwargs):
        url = SWSCAN_BASE + index
        resp = await self.get(url, headers=headers, return_type="text", **kwargs)

        return loads(bytes(resp, "utf-8"))
