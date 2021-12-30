from bs4 import BeautifulSoup
from requests import get


def test():
    a = get(
        "https://swdist.apple.com/content/downloads/41/23/061-26578-A_FF0C6M87LS/ylvl0phx6uy3i444qt9p57n8wz0xnylmd9/061-26578.English.dist"
    ).text

    s = BeautifulSoup(a, "html.parser")

    return (
        a.split("<key>BUILD</key>")[1]
        .split("</string>")[0]
        .replace("<string>", "")
        .strip()
    )


print(test())
