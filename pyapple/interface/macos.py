from hurry.filesize import alternative, size

from .base import BaseModel


class MacOSProduct(BaseModel):
    def __init__(self, product_id) -> None:
        self.product_id = product_id
        self.title = ""
        self.version = ""
        self.buildid = ""
        self.upload_date = ""
        self.packages = []


class Package(BaseModel):
    def __init__(self, url: str, filesize: int) -> None:
        self.filename = url.split("/")[-1]
        self.url = url
        self.filesize = (filesize, size(filesize, system=alternative))
