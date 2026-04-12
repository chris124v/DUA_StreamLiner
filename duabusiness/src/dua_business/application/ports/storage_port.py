"""Port for file storage operations (Google Cloud Storage)."""

from typing import Protocol, Optional, BinaryIO


class StoragePort(Protocol):
    """Protocol for file storage operations."""

    async def upload_file(self, path: str, content: bytes) -> str:
        """Upload file to storage.

        Args:
            path: Storage path for the file
            content: File content as bytes

        Returns:
            Public URI of uploaded file
        """
        ...

    async def download_file(self, path: str) -> bytes:
        """Download file from storage.

        Args:
            path: Storage path of the file

        Returns:
            File content as bytes
        """
        ...

    async def delete_file(self, path: str) -> None:
        """Delete file from storage.

        Args:
            path: Storage path of the file
        """
        ...

    async def file_exists(self, path: str) -> bool:
        """Check if file exists.

        Args:
            path: Storage path of the file

        Returns:
            True if file exists, False otherwise
        """
        ...

    async def get_download_url(self, path: str) -> str:
        """Get download URL for file.

        Args:
            path: Storage path of the file

        Returns:
            Download URL
        """
        ...
