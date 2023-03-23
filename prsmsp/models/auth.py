class APIKeyAuth:
    def __init__(
        self,
        api_key,
    ) -> None:
        self.api_key = api_key


class UnamePassAuth:
    def __init__(
        self,
        username,
        password,
    ) -> None:
        self.username = username
        self.password = password
