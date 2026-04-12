"""Port for Unit of Work pattern (database transactions)."""

from typing import Protocol


class UnitOfWorkPort(Protocol):
    """Protocol for Unit of Work pattern."""

    async def begin(self) -> None:
        """Begin a transaction."""
        ...

    async def commit(self) -> None:
        """Commit the transaction."""
        ...

    async def rollback(self) -> None:
        """Rollback the transaction."""
        ...

    async def __aenter__(self):
        """Context manager entry."""
        ...

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        ...
