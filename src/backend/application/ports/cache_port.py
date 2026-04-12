"""Port for caching operations (Redis)."""

from typing import Protocol, Optional, Any


class CachePort(Protocol):
    """Protocol for caching operations."""

    async def get(self, key: str) -> Optional[str]:
        """Get value from cache.

        Args:
            key: Cache key

        Returns:
            Cached value or None if not found
        """
        ...

    async def set(
        self, key: str, value: str, ttl_seconds: Optional[int] = None
    ) -> None:
        """Set value in cache.

        Args:
            key: Cache key
            value: Value to cache
            ttl_seconds: Time to live in seconds
        """
        ...

    async def delete(self, key: str) -> None:
        """Delete value from cache.

        Args:
            key: Cache key
        """
        ...

    async def exists(self, key: str) -> bool:
        """Check if key exists in cache.

        Args:
            key: Cache key

        Returns:
            True if key exists, False otherwise
        """
        ...

    async def clear(self, pattern: Optional[str] = None) -> None:
        """Clear cache.

        Args:
            pattern: Optional pattern to match keys for deletion
        """
        ...
