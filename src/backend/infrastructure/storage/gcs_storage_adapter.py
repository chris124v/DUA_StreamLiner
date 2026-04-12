"""Adapter for Google Cloud Storage operations."""

import logging
from typing import Optional, BinaryIO

logger = logging.getLogger(__name__)


class GCSStorageAdapter:
    """Adapter for Google Cloud Storage."""

    def __init__(self, project_id: str, bucket_name: str):
        """Initialize GCS adapter.

        Args:
            project_id: Google Cloud project ID
            bucket_name: GCS bucket name
        """
        self.project_id = project_id
        self.bucket_name = bucket_name

    async def upload_file(self, path: str, content: bytes) -> str:
        """Upload file to GCS.

        Args:
            path: Storage path for the file
            content: File content as bytes

        Returns:
            Public URI of uploaded file
        """
        # Stub implementation
        pass

    async def download_file(self, path: str) -> bytes:
        """Download file from GCS.

        Args:
            path: Storage path of the file

        Returns:
            File content as bytes
        """
        # Stub implementation
        pass

    async def delete_file(self, path: str) -> None:
        """Delete file from GCS.

        Args:
            path: Storage path of the file
        """
        # Stub implementation
        pass

    async def file_exists(self, path: str) -> bool:
        """Check if file exists in GCS.

        Args:
            path: Storage path of the file

        Returns:
            True if file exists, False otherwise
        """
        # Stub implementation
        pass

    async def get_download_url(self, path: str) -> str:
        """Get download URL for file.

        Args:
            path: Storage path of the file

        Returns:
            Download URL (signed or public)
        """
        # Stub implementation
        pass

    async def list_files(self, prefix: str) -> list[str]:
        """List files with given prefix.

        Args:
            prefix: Path prefix

        Returns:
            List of file paths
        """
        # Stub implementation
        pass
