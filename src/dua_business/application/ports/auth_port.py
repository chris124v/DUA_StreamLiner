from typing import Protocol

class AuthPort(Protocol):
    def validate_token(self, token: str) -> dict: ...

