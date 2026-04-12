"""Domain services for session and authentication."""

from abc import ABC, abstractmethod
from typing import Optional
from datetime import datetime


class SessionService(ABC):
    """Abstract service for session management."""

    @abstractmethod
    async def create_session(self, user_id: str) -> str:
        """Create a new session for a user.

        Args:
            user_id: The user ID

        Returns:
            Session ID
        """
        pass

    @abstractmethod
    async def validate_session(self, session_id: str) -> bool:
        """Validate an existing session.

        Args:
            session_id: The session ID to validate

        Returns:
            True if valid, False otherwise
        """
        pass

    @abstractmethod
    async def invalidate_session(self, session_id: str) -> None:
        """Invalidate a session.

        Args:
            session_id: The session ID to invalidate
        """
        pass

    @abstractmethod
    async def get_session_user_id(self, session_id: str) -> Optional[str]:
        """Get the user ID associated with a session.

        Args:
            session_id: The session ID

        Returns:
            User ID or None if session not found
        """
        pass


class AuthenticationService(ABC):
    """Abstract service for authentication operations."""

    @abstractmethod
    async def verify_jwt(self, token: str) -> dict:
        """Verify and decode a JWT token.

        Args:
            token: The JWT token to verify

        Returns:
            Dictionary containing token claims
        """
        pass

    @abstractmethod
    async def get_user_permissions(self, user_id: str) -> list[str]:
        """Get user permissions.

        Args:
            user_id: The user ID

        Returns:
            List of permission codes
        """
        pass

    @abstractmethod
    async def has_permission(
        self, user_id: str, permission_code: str
    ) -> bool:
        """Check if user has a specific permission.

        Args:
            user_id: The user ID
            permission_code: The permission code to check

        Returns:
            True if user has permission, False otherwise
        """
        pass
