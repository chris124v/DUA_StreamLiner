"""Domain services for DUA generation and file handling."""

from abc import ABC, abstractmethod
from typing import Optional, BinaryIO
from datetime import datetime


class FileStorageService(ABC):
    """Abstract service for file storage operations."""

    @abstractmethod
    async def upload_file(
        self, file_name: str, file_stream: BinaryIO, user_id: str
    ) -> str:
        """Upload a file to storage.

        Args:
            file_name: The name of the file
            file_stream: The file content stream
            user_id: The user ID uploading the file

        Returns:
            Storage path or file ID
        """
        pass

    @abstractmethod
    async def download_file(self, storage_path: str) -> BinaryIO:
        """Download a file from storage.

        Args:
            storage_path: The path to the file in storage

        Returns:
            File stream
        """
        pass

    @abstractmethod
    async def delete_file(self, storage_path: str) -> None:
        """Delete a file from storage.

        Args:
            storage_path: The path to the file in storage
        """
        pass


class DUAGenerationService(ABC):
    """Abstract service for DUA document generation."""

    @abstractmethod
    async def create_dua_document(
        self, generation_id: str, template_version: str, field_mappings: dict
    ) -> bytes:
        """Create a DUA document with populated fields.

        Args:
            generation_id: The generation session ID
            template_version: The version of DUA template to use
            field_mappings: Dictionary of field name to extracted value

        Returns:
            Generated document as bytes
        """
        pass

    @abstractmethod
    async def apply_formatting_rules(
        self, field_name: str, field_value: str
    ) -> str:
        """Apply formatting rules to a field value.

        Args:
            field_name: The field name
            field_value: The value to format

        Returns:
            Formatted value
        """
        pass

    @abstractmethod
    async def get_confidence_indicator(
        self, confidence_score: float
    ) -> str:
        """Get warning indicator based on confidence score.

        Args:
            confidence_score: The confidence score (0-1)

        Returns:
            Indicator string: "green", "yellow", or "red"
        """
        pass


class TemplateManagementService(ABC):
    """Abstract service for DUA template management."""

    @abstractmethod
    async def get_template_version(
        self, process_type: str
    ) -> str:
        """Get the current template version.

        Args:
            process_type: Either 'import' or 'export'

        Returns:
            Template version string
        """
        pass

    @abstractmethod
    async def load_template(
        self, process_type: str, template_version: str
    ) -> dict:
        """Load a DUA template.

        Args:
            process_type: Either 'import' or 'export'
            template_version: The template version to load

        Returns:
            Dictionary containing template structure
        """
        pass

    @abstractmethod
    async def validate_template_update(
        self, new_template: dict
    ) -> bool:
        """Validate that a template update is compatible.

        Args:
            new_template: The new template to validate

        Returns:
            True if template is valid, False otherwise
        """
        pass
