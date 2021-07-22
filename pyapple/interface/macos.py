import dataclasses
from typing import List, Optional


@dataclasses.dataclass(repr=True)
class Package:
    """Dataclass object of product package.

    Attributes:
        url (str): URL link of the package file.
        filesize (int): Size of the package file.
        filename (str): Filename of the package file.
    """

    __slots__ = ("url", "filesize", "filename")

    url: str
    filesize: int

    def __post_init__(self):
        self.filename = self.url.split("/")[-1]


@dataclasses.dataclass(repr=True)
class MacOSProduct:
    """Dataclass object of a single macOS product.

    Attributes:
        product_id (str): Product ID of the macOS product.
        title (str): Title of the macOS product.
        version (str): macOS version of the product.
        buildid (str): Build string of the macOS product.
        postdate (datetime.datetime): Posted date of the macOS product.
        packages (List[Package]): List of packages of the macOS product.
    """

    __slots__ = ("product_id", "title", "version", "buildid", "postdate", "packages")

    product_id: str
    title: str
    version: str
    buildid: str
    postdate: any
    packages: Optional[List[Package]]
