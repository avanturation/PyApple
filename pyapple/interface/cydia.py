from typing import Optional, Union

from .base import BaseModel, to_dt


class Repo(BaseModel):
    def __init__(
        self,
        label,
        suite,
        version,
        codename,
        architectures,
        description,
        icon,
        repo,
        package_count,
        section_count,
        sections,
    ) -> None:
        self.label = label
        self.suite = suite
        self.version = version
        self.codename = codename
        self.architectures = architectures
        self.description = description
        self.icon = icon
        self.repo = repo
        self.package_count = package_count
        self.section_count = section_count
        self.sections = sections


class Builds(BaseModel):
    def __init__(
        self, filename, size, md5sum, sha1, sha256, installed_size, version, status
    ) -> None:
        self.filename = filename
        self.size = size
        self.md5sum = md5sum
        self.sha1 = sha1
        self.sha256 = sha256
        self.installed_size = installed_size
        self.version = version
        self.status = status


class Tweak(BaseModel):
    def __init__(
        self,
        architecture,
        author,
        depends,
        depiction,
        description,
        icon,
        maintainer,
        name,
        package,
        section,
        version,
        builds,
    ) -> None:
        self.architecture = architecture
        self.author = author
        self.depends = depends
        self.depiction = depiction
        self.description = description
        self.icon = icon
        self.maintainer = maintainer
        self.name = name
        self.package = package
        self.section = section
        self.version = version
        self.builds = builds
