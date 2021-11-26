import dataclasses
from typing import List, Optional


@dataclasses.dataclass(repr=True)
class Package:
    """
    Dataclass object of product package.

    **Note: An element `filename` which contains package's filename will be created after `__post_init__`.**
    """

    __slots__ = ("url", "filesize", "filename")

    url: str
    """URL link of the package file."""
    filesize: int
    """Size of the package file."""

    def __post_init__(self):
        self.filename = self.url.split("/")[-1]


@dataclasses.dataclass(repr=True)
class MacOSProduct:
    """
    Dataclass object of a single macOS product.
    """

    __slots__ = ("product_id", "title", "version", "buildid", "postdate", "packages")

    product_id: str
    """Product ID of the macOS product."""
    title: str
    """Title of the macOS product."""
    version: str
    """macOS version of the product."""
    buildid: str
    """Build string of the macOS product."""
    postdate: any
    """Posted date of the macOS product."""
    packages: Optional[List[Package]]
    """List of packages of the macOS product."""
