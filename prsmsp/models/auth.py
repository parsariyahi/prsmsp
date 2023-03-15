class APIKeyAuth:
    
    def __init__(
        self,
        key
    ) -> None:
        self.key = key

class PassAuth:
    
    def __init__(
        self,
        username,
        password,
    ) -> None:
        self.username = username
        self.password = password

class AuthFactory:

    @staticmethod
    def get(auth_type):
        auth_types = {
            'api_key': APIKeyAuth,
            'pass': PassAuth,
        }

        Auth = auth_types.get(auth_type, None)

        if Auth is None: # if the auth method is not supported
            raise ValueError

        # this will not initiate the object, its just returning.
        # if you write like Auth() it will be initiated.
        # this will avoid the Input Error Execption.
        return Auth