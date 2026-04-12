"""Application services for coordinating domain logic and use cases."""

from abc import ABC, abstractmethod
from typing import Optional, list
from dua_business.application.dto.dto_models import (
    GenerationStatusDTO,
    GenerationResultDTO,
)


class DUAGenerationApplicationService(ABC):
    """Application service for orchestrating DUA generation workflow."""

    @abstractmethod
    async def initiate_generation(
        self, user_id: str, process_type: str
    ) -> str:
        """Initiate a new DUA generation process.

        Args:
            user_id: The user initiating the process
            process_type: 'import' or 'export'

        Returns:
            Generation session ID
        """
        pass

    @abstractmethod
    async def process_uploaded_documents(
        self, generation_id: str, document_paths: list[str]
    ) -> dict:
        """Process uploaded documents through the pipeline.

        Args:
            generation_id: The generation session ID
            document_paths: List of paths to uploaded documents

        Returns:
            Processing result with document statistics
        """
        pass

    @abstractmethod
    async def get_generation_status(
        self, generation_id: str
    ) -> GenerationStatusDTO:
        """Get current status of a generation process.

        Args:
            generation_id: The generation session ID

        Returns:
            Current generation status
        """
        pass

    @abstractmethod
    async def complete_generation(
        self, generation_id: str
    ) -> GenerationResultDTO:
        """Finalize generation and prepare results.

        Args:
            generation_id: The generation session ID

        Returns:
            Final generation result
        """
        pass

    @abstractmethod
    async def cancel_generation(self, generation_id: str) -> None:
        """Cancel an ongoing generation process.

        Args:
            generation_id: The generation session ID
        """
        pass


class DocumentProcessingApplicationService(ABC):
    """Application service for document processing pipeline."""

    @abstractmethod
    async def classify_documents(
        self, generation_id: str, document_ids: list[str]
    ) -> dict:
        """Classify documents into categories.

        Args:
            generation_id: The generation session ID
            document_ids: List of document IDs to classify

        Returns:
            Classification results
        """
        pass

    @abstractmethod
    async def extract_document_fields(
        self, generation_id: str, document_id: str
    ) -> dict:
        """Extract customs fields from a document.

        Args:
            generation_id: The generation session ID
            document_id: The document to process

        Returns:
            Extracted fields with confidence scores
        """
        pass

    @abstractmethod
    async def perform_ocr(
        self, generation_id: str, document_id: str
    ) -> str:
        """Perform OCR on image or PDF documents.

        Args:
            generation_id: The generation session ID
            document_id: The document to process

        Returns:
            Extracted text from OCR
        """
        pass


class FieldMappingApplicationService(ABC):
    """Application service for mapping extracted fields to DUA template."""

    @abstractmethod
    async def map_fields_to_template(
        self, generation_id: str, extracted_fields: dict
    ) -> dict:
        """Map extracted fields to DUA template sections.

        Args:
            generation_id: The generation session ID
            extracted_fields: Dictionary of extracted fields

        Returns:
            Field mappings with confidence indicators
        """
        pass

    @abstractmethod
    async def validate_field_mappings(
        self, generation_id: str
    ) -> dict:
        """Validate all field mappings for a generation.

        Args:
            generation_id: The generation session ID

        Returns:
            Validation results
        """
        pass
