class HTTPException(Exception):
    def __init__(self, code, url) -> None:
        self.error = f"While requesting to {url}, request returned status {code}."

    def __str__(self) -> str:
        return self.error


class OSException(Exception):
    def __init__(self) -> None:
        self.error = "Your operating system does not support this function. Only Linux and macOS supports."

    def __str__(self) -> str:
        return self.error
