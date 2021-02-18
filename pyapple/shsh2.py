import asyncio
from typing import Coroutine, Optional


class SHSH2:
    def __init__(
        self, ecid: str, apnonce: Optional[str], model: str, version: str
    ) -> None:
        self.model = model
        self.ecid = ecid
        self.apnonce = apnonce
        self.version = version

    async def get_shsh2_blob(self) -> Coroutine:
        cmd = [
            "bin/tsschecker",
            "-d",
            self.model,
            "-e",
            self.ecid,
            "-s -i",
            self.version,
        ]
        
        if self.apnonce:
            cmd.append("--apnonce")
            cmd.append(self.apnonce)

        subp = await asyncio.create_subprocess_shell(
            " ".join(cmd),
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )

        return await subp.communicate()
