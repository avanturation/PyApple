from asyncio import create_subprocess_shell, subprocess


class SHSH2:
    def __init__(self) -> None:
        super().__init__()

    async def run_tsschecker(self, **kwargs):
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
    ):
        args = ["tsschecker", "-d", identifier, "-e", ecid, "--buildid", buildid]
