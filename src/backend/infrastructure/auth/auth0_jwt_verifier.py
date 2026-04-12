from dua_business.application.ports.auth_port import AuthPort

class Auth0JwtVerifierAdapter(AuthPort):
    def validate_token(self, token: str) -> dict:
        _ = token
        raise NotImplementedError("Contract only")

