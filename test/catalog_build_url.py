CATLOG_SUF = {
    "publicseed": "beta",
    "publicrelease": "",
    "customerseed": "customerseed",
    "developerseed": "seed",
}

MACOS_NAME = {
    "8": "mountainlion",
    "7": "lion",
    "6": "snowleopard",
    "5": "leopard",
}

MACOS_FULLNAME = {
    "tiger": "10.4",
    "leopard": "10.5",
    "snow leopard": "10.6",
    "lion": "10.7",
    "mountain lion": "10.8",
    "mavericks": "10.9",
    "yosemite": "10.10",
    "el capitan": "10.11",
    "sierra": "10.12",
    "high sierra": "10.13",
    "mojave": "10.14",
    "catalina": "10.15",
    "big sur": "10.16",
    # "macos12_candidate1": "10.17",
    # "macos12_candidate2": "12.0",
}


def build_url(catalog_id) -> str:
    catalog = catalog_id.lower()
    url = "https://swscan.apple.com/content/catalogs/others/index-12"

    if CATLOG_SUF[catalog]:
        url = url.replace("12", "12" + CATLOG_SUF[catalog] + "-12-")

    url += "-".join(
        [
            MACOS_NAME[str(x)] if str(x) in MACOS_NAME else "10." + str(x)
            for x in reversed(range(5, 16 + 1))
        ]
    )

    url += ".merged-1.sucatalog"

    return url


print(build_url("developerseed"))
