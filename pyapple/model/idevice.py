from typing import Optional


class iDevice:
    def __init__(
        self,
        name: str,
        identifier: str,
        boardconfig: str,
        platform: str,
        cpid: str,
        bdid: str,
        firmwares: Optional[list],
    ) -> None:
        self.name = name
        self.identifier = identifier
        self.boardconfig = boardconfig
        self.platform = platform
        self.cpid = cpid
        self.bdid = bdid
        self.firmwares = firmwares