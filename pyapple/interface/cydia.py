import dataclasses
from typing import List, Optional


@dataclasses.dataclass(init=True, repr=True)
class Repo:
    __slots__ = (
        "label",
        "suite",
        "version",
        "codename",
        "architectures",
        "components",
        "description",
        "icon",
        "repo",
        "package_count",
        "section_count",
        "sections",
    )

    label: Optional[str]
    suite: Optional[str]
    version: Optional[str]
    codename: Optional[str]
    architectures: Optional[str]
    components: Optional[str]
    description: Optional[str]
    icon: Optional[str]
    repo: Optional[str]
    package_count: Optional[int]
    section_count: Optional[int]
    sections: Optional[List]

    def __init__(self, **kwargs) -> None:
        fields = [field.name for field in dataclasses.fields(self)]

        for key, value in kwargs.items():
            if key in fields:
                setattr(self, key, value)


@dataclasses.dataclass(init=True, repr=True)
class Builds:
    __slots__ = (
        "filename",
        "size",
        "md5sum",
        "sha1",
        "sha256",
        "installed_size",
        "version",
        "status",
    )

    filename: Optional[str]
    size: Optional[str]
    md5sum: Optional[str]
    sha1: Optional[any]
    sha256: Optional[str]
    installed_size: Optional[str]
    version: Optional[str]
    status: Optional[any]

    def __init__(self, **kwargs) -> None:
        fields = [field.name for field in dataclasses.fields(self)]

        for key, value in kwargs.items():
            if key in fields:
                setattr(self, key, value)


@dataclasses.dataclass(init=True, repr=True)
class Tweak:
    __slots__ = (
        "architecture",
        "author",
        "depends",
        "depiction",
        "description",
        "icon",
        "maintainer",
        "name",
        "package",
        "section",
        "version",
        "builds",
    )

    architecture: Optional[str]
    author: Optional[str]
    depends: Optional[List[str]]
    depiction: Optional[str]
    description: Optional[str]
    icon: Optional[str]
    maintainer: Optional[str]
    name: Optional[str]
    package: Optional[str]
    section: Optional[str]
    version: Optional[str]
    builds: Optional[List[Builds]]

    def __init__(self, **kwargs) -> None:
        fields = [field.name for field in dataclasses.fields(self)]

        for key, value in kwargs.items():
            if key in fields:
                setattr(self, key, value)
