"""Port for OCR processing (Google Cloud Document AI)."""

from typing import Protocol


class OCRPort(Protocol):
    """Protocol for OCR operations."""

    async def extract_text(self, file_uri: str) -> str:
        """Extract text from document.

        Args:
            file_uri: URI to file in Cloud Storage

        Returns:
            Extracted text
        """
        ...

    async def extract_with_layout(self, file_uri: str) -> dict:
        """Extract text with layout information.

        Args:
            file_uri: URI to file in Cloud Storage

        Returns:
            Dictionary with text, layout, bounding boxes
        """
        ...

    async def extract_tables(self, file_uri: str) -> list[dict]:
        """Extract tables from document.

        Args:
            file_uri: URI to file in Cloud Storage

        Returns:
            List of detected tables with content
        """
        ...

    async def process_document(self, file_uri: str) -> dict:
        """Perform full document processing.

        Args:
            file_uri: URI to file in Cloud Storage

        Returns:
            Complete OCR results
        """
        ...
