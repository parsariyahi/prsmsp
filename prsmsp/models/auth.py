class APIKeyAuth:
    
    def __init__(
        self,
        token
    ) -> None:
        self.token = token

class PassAuth:
    
    def __init__(
        self,
        username,
        password
    ) -> None:
        self.username = username
        self.password = password

class Auth :

    def __init__(
        self,
        auth_type,
        **auth_info,
    ) -> None:
        if auth_type == 'token':
            token = auth_info.get('token', '')
            if not token:
                raise ValueError
            self.auth = TokenAuth(token)
            return None

        elif auth_type == 'pass':
            username = auth_info.get('username', '')
            password = auth_info.get('password', '')
            if not username and not password :
                raise ValueError
            self.auth = PassAuth(username, password)
            return None

        raise ValueError
        
    def get_auth_info(self):
        if isinstance(self.auth, (TokenAuth, UPAuth)) :
            return self.auth

        return None