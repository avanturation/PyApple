class HTTPException(Exception):
    """
    Exception which happens when HTTP status code is not 200 (OK).
    """

    def __init__(self, code, url) -> None:
        self.error = f"While requesting to {url}, request returned status {code}."

    def __str__(self) -> str:
        return self.error


class NoCatalogResult(Exception):
    """
    Exception which happens when there is no product with given product id.
    """

    def __init__(self, product_id) -> None:
        self.error = f"There is no catalog result with id {product_id}."

    def __str__(self) -> str:
        return self.error
