from typing import List, Optional

import dataclasses


@dataclasses.dataclass(repr=True)
class Package:
    __slots__ = ("url", "filesize", "filename")

    url: str
    filesize: int

    def __post_init__(self):
        self.filename = self.url.split("/")[-1]


@dataclasses.dataclass(repr=True)
class MacOSProduct:
    __slots__ = ("product_id", "title", "version", "buildid", "postdate", "packages")

    product_id: str
    title: str
    version: str
    buildid: str
    postdate: any
    packages: Optional[List[Package]]
