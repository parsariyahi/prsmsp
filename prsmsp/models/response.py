class Response:
    """an unified Response model for every panels"""

    __dict__ = ("status_code", "real_resp")

    def __init__(
        self,
        status_code: int,
        real_resp: dict,
    ) -> None:
        """TODO write doc string"""
        self.status_code = status_code
        self.real_resp = real_resp

    def __eq__(self, other) -> bool:
        """checks the equality of two Response object"""
        if isinstance(other, Response):
            return self.status_code == other.status_code
        raise TypeError

    def get_real_resp(self):
        return self.real_resp
