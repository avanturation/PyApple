from typing import List, Optional
from .base import BaseModel


class MacOSProduct(BaseModel):
    def __init__(
        self, product_id: str, title: str, version: str, buildid: str, postdate, packages=Optional[List]
    ) -> None:
        self.product_id = product_id
        self.title = title
        self.version = version
        self.buildid = buildid
        self.postdate = postdate
        self.packages = packages


class Package(BaseModel):
    def __init__(self, url: str, filesize: int) -> None:
        self.filename = url.split("/")[-1]
        self.url = url
        self.filesize = filesize
