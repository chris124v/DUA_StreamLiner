from dataclasses import dataclass


@dataclass
class User:
    user_id: str
    auth0_id: str
    role: str
