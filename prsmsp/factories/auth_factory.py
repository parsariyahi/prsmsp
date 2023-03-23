from prsmsp.models.auth import APIKeyAuth, UnamePassAuth


class AuthFactory:
    """AuthFactory."""

    @staticmethod
    def get(auth_type: str):
        """Static method to get the class of authentication.

        :param auth_type:
        :type auth_type: str
        """
        auth_types = {
            "api_key": APIKeyAuth,
            "username_pass": UnamePassAuth,
        }

        Auth = auth_types.get(auth_type, None)

        if Auth is None:
            # if the auth method is not supported
            raise ValueError

        # this will not initiate the object, its just returning.
        # if you write like Auth() it will be initiated.
        # this will avoid the Input Error Execption.
        return Auth
