"""Port for authentication operations (Auth0)."""

from typing import Protocol, Optional


class AuthPort(Protocol):
    """Protocol for authentication operations."""

    async def validate_token(self, token: str) -> dict:
        """Validate JWT token.

        Args:
            token: JWT token to validate

        Returns:
            Token claims dictionary
        """
        ...

    async def get_user_info(self, user_id: str) -> dict:
        """Get user information from Auth0.

        Args:
            user_id: User ID

        Returns:
            User information dictionary
        """
        ...

    async def get_user_roles(self, user_id: str) -> list[str]:
        """Get user roles.

        Args:
            user_id: User ID

        Returns:
            List of role identifiers
        """
        ...

    async def get_user_permissions(self, user_id: str) -> list[str]:
        """Get user permissions.

        Args:
            user_id: User ID

        Returns:
            List of permission codes
        """
        ...
