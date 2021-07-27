import dataclasses
from typing import List, Optional


@dataclasses.dataclass(init=True, repr=True)
class Repo:
    """Dataclass object of Cydia/Slieo repository.

    Attributes:
        label (str): Label of the repository.
        suite (str): Status of the repository.
        version (str): Version of the repository.
        codename (str): Codename of the repository.
        architectures (str): Available architectures from the repository.
        components (str): Components of the repository.
        description (str): Description of the repository.
        icon: (str): URL of the icon of the repository.
        repo (str): URL of the repository.
        package_count (int): Numbers of all available tweaks from the repository.
        section_count (int): Numbers of all available sections from the repository.
        sections (List): Lists of all available sections from the repository.
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
    """Dataclass of single build of a tweak.

    Attributes:
        filename (str): Filename of the build.
        size (str): Size of the build file.
        md5sum (str): MD5sum of the build file.
        sha1 (str): SHA1 of the build file.
        sha256 (str): SHA256 of the build file.
        installed_size (str): Installed size of the build file.
        version (str): Version of the build.
        status (any): Current status of the build.
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
    """Dataclass object of a tweak.

    Attributes:
        architecture (str): Target architecture of the tweak.
        author (str): Author of the tweak.
        depends (List[str]): Dependencies of the tweak.
        depiction (str): Depiction of the tweak.
        description (str): Description of the tweak.
        icon (str): URL of the tweak's icon.
        maintainer (str): Maintainer of the tweal.
        name (str): Name of the tweak.
        package (str): Package ID of the tweak.
        section (str): Section string where the tweak is located.
        version (str): Version of the tweak.
        builds (List[Builds]): All builds from the tweak.
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
