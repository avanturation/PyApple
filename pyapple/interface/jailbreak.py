import dataclasses
from typing import List, Optional


@dataclasses.dataclass(init=True, repr=True)
class Repo:
    """
    Dataclass object of Cydia/Slieo repository.
    """

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
    """Label of the repository."""
    suite: Optional[str]
    """Status of the repository."""
    version: Optional[str]
    """Version of the repository."""
    codename: Optional[str]
    """Codename of the repository."""
    architectures: Optional[str]
    """Available architectures from the repository."""
    components: Optional[str]
    """Components of the repository."""
    description: Optional[str]
    """Description of the repository."""
    icon: Optional[str]
    """URL of the icon of the repository."""
    repo: Optional[str]
    """URL of the repository."""
    package_count: Optional[int]
    """Numbers of all available tweaks from the repository."""
    section_count: Optional[int]
    """Numbers of all available sections from the repository."""
    sections: Optional[List]
    """Lists of all available sections from the repository."""

    def __init__(self, **kwargs) -> None:
        fields = [field.name for field in dataclasses.fields(self)]

        for key, value in kwargs.items():
            if key in fields:
                setattr(self, key, value)


@dataclasses.dataclass(init=True, repr=True)
class Builds:
    """
    Dataclass of single build of a tweak.
    """

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
    """Filename of the build."""
    size: Optional[str]
    """Size of the build file."""
    md5sum: Optional[str]
    """MD5sum of the build file."""
    sha1: Optional[any]
    """SHA1 of the build file."""
    sha256: Optional[str]
    """SHA256 of the build file."""
    installed_size: Optional[str]
    """Installed size of the build file."""
    version: Optional[str]
    """Version of the build."""
    status: Optional[any]
    """Current status of the build."""

    def __init__(self, **kwargs) -> None:
        fields = [field.name for field in dataclasses.fields(self)]

        for key, value in kwargs.items():
            if key in fields:
                setattr(self, key, value)


@dataclasses.dataclass(init=True, repr=True)
class Tweak:
    """
    Dataclass object of a tweak.
    """

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
    """Target architecture of the tweak."""
    author: Optional[str]
    """Author of the tweak."""
    depends: Optional[List[str]]
    """Dependencies of the tweak."""
    depiction: Optional[str]
    """Depiction of the tweak."""
    description: Optional[str]
    """Description of the tweak."""
    icon: Optional[str]
    """URL of the tweak's icon."""
    maintainer: Optional[str]
    """Maintainer of the tweak."""
    name: Optional[str]
    """Name of the tweak."""
    package: Optional[str]
    """Package ID of the tweak."""
    section: Optional[str]
    """Section where the tweak is located."""
    version: Optional[str]
    """Version of the tweak."""
    builds: Optional[List[Builds]]
    """All builds from the tweak."""

    def __init__(self, **kwargs) -> None:
        fields = [field.name for field in dataclasses.fields(self)]

        for key, value in kwargs.items():
            if key in fields:
                setattr(self, key, value)
