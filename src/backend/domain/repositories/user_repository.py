from typing import Protocol

from dua_business.domain.entities.user import User


class UserRepository(Protocol):
    def get_by_auth0_id(self, auth0_id: str) -> User | None: ...
