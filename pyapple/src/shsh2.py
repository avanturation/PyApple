from asyncio import create_subprocess_shell, subprocess
from typing import Optional


class SHSH2:
    """Class for tsschecker related functions."""

    def __init__(self) -> None:
        super().__init__()

    async def run_tsschecker(self, **kwargs):
        """Runs tsschecker from your device.

        Args:
            **Same as normal tsschecker.**

        Returns:
            asyncio.subprocess.Process: Subprocess object of executed tsschecker.
        """

        args = ["tsschecker"]

        if kwargs.get("device"):
            args.append("-d")
            args.append(kwargs.get("device"))

        if kwargs.get("ios"):
            args.append("-i")
            args.append(kwargs.get("ios"))

        if kwargs.get("buildid"):
            args.append("-Z")
            args.append(kwargs.get("buildid"))

        if kwargs.get("boardconfig"):
            args.append("-B")
            args.append(kwargs.get("boardconfig"))

        if kwargs.get("ota"):
            args.append("-o")

        if kwargs.get("no_baseband"):
            args.append("-b")

        if kwargs.get("build_manifest"):
            args.append("-m")

        if kwargs.get("save"):
            args.append("-s")

        if kwargs.get("update_install"):
            args.append("-u")

        if kwargs.get("latest"):
            args.append("-l")

        if kwargs.get("ecid"):
            args.append("-e")
            args.append(kwargs.get("ecid"))

        if kwargs.get("generator"):
            args.append("-g")
            args.append(kwargs.get("generator"))

        if kwargs.get("apnonce"):
            args.append("--apnonce")
            args.append(kwargs.get("apnonce"))

        if kwargs.get("sepnonce"):
            args.append("--sepnonce")
            args.append(kwargs.get("sepnonce"))

        if kwargs.get("bbsnum"):
            args.append("--bbsnum")
            args.append(kwargs.get("bbsnum"))

        if kwargs.get("beta"):
            args.append("--beta")

        if kwargs.get("nocache"):
            args.append("--nocache")

        if kwargs.get("print_tss_request"):
            args.append("--print-tss-request")

        if kwargs.get("print_tss_response"):
            args.append("--print-tss-response")

        if kwargs.get("raw"):
            args.append("--raw")

        proc = await create_subprocess_shell(
            " ".join(args),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

        return proc

    async def save_blobs(
        self,
        ecid: str,
        identifier: str,
        buildid: str,
        boardconfig: Optional[str] = None,
        apnonce: Optional[str] = None,
        generator: Optional[str] = None,
        ota: Optional[bool] = False,
        beta: Optional[bool] = False,
    ):
        """Save SHSH2 blobs of specific iOS/iPadOS version for your device.

        Args:
            ecid (str): ECID of your iDevice.
            identifier (str): Identifier of iDevice. (e.g. iPhone12,1)
            buildid (str): Build ID of IPSW firmware. (e.g. 19A5297e)
            boardconfig (Optional[str], optional): Boardconfig of your iDevice. If boardconfig is None, it automatically searches from ipsw.me.
            apnonce (Optional[str], optional): (For A12 Bionic or above) Apnonce of your device. Defaults to None.
            generator (Optional[str], optional): (For A12 Bionic or above) Boot nonce of your device. Defaults to None.
            ota (Optional[bool], optional): Saves SHSH2 blobs for OTA build. Defaults to False.
            beta (Optional[bool], optional): Saves SHSH2 blobs for beta build of iOS/iPadOS. Defaults to False.

        Returns:
            asyncio.subprocess.Process: Subprocess object of executed tsschecker.
        """

        args = ["tsschecker", "-d", identifier, "-e", ecid, "--buildid", buildid]

        if apnonce:
            args.append("--apnonce")
            args.append(apnonce)

        if generator:
            args.append("--generator")
            args.append(generator)

        if ota:
            args.append("-o")

        if beta:
            args.append("--beta")

        if boardconfig is None:
            device_info = await self.__HTTP.ipsw(
                endpoint=f"/device/{identifier}", return_type="json"
            )

            boardconfig = device_info["boardconfig"]

        args.append("-B")
        args.append(boardconfig)

        proc = await create_subprocess_shell(
            " ".join(args),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

        await self.__HTTP.session.close()
        return proc

    async def latest_blobs(
        self,
        identifier: str,
        ecid: str,
        apnonce: Optional[str] = None,
        generator: Optional[str] = None,
        boardconfig: Optional[str] = None,
    ):
        """Extracts shsh2 blobs for latest version.

        Args:
            identifier (str): Identifier of iDevice. (e.g. iPhone12,1)
            ecid (str): ECID of your iDevice.
            apnonce (Optional[str], optional): (For A12 Bionic or above) Apnonce of your device. Defaults to None.
            generator (Optional[str], optional): (For A12 Bionic or above) Boot nonce of your device. Defaults to None.
            boardconfig (Optional[str], optional): Boardconfig of your iDevice. If boardconfig is None, it automatically searches from ipsw.me.

        Returns:
            asyncio.subprocess.Process: Subprocess object of executed tsschecker.
        """

        args = ["tsschecker", "-d", identifier, "-e", ecid]

        device_info = await self.__HTTP.ipsw(
            endpoint=f"/device/{identifier}", return_type="json"
        )

        latest_firmware = device_info["firmwares"][0]

        buildid = latest_firmware["buildid"]
        version = latest_firmware["version"]

        args.append("--buildid")
        args.append(buildid)

        args.append("-i")
        args.append(version)

        if apnonce:
            args.append("--apnonce")
            args.append(apnonce)

        if generator:
            args.append("--generator")
            args.append(generator)

        if boardconfig is None:
            boardconfig = device_info["boardconfig"]

        args.append("-B")
        args.append(boardconfig)

        proc = await create_subprocess_shell(
            " ".join(args),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

        await self.__HTTP.session.close()
        return proc
