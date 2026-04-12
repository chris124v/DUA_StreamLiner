"""Domain services for document processing and field extraction."""

from abc import ABC, abstractmethod
from typing import Optional, list
from dua_business.domain.value_objects import DocumentBlock, ExtractedField


class DocumentProcessingService(ABC):
    """Abstract service for processing documents."""

    @abstractmethod
    async def classify_document_block(
        self, block: DocumentBlock
    ) -> dict[str, float]:
        """Classify a document block into categories.

        Args:
            block: The document block to classify

        Returns:
            Dictionary mapping category names to confidence scores
        """
        pass

    @abstractmethod
    async def calculate_block_hash(self, content: str) -> str:
        """Calculate hash for a document block.

        Args:
            content: The content to hash

        Returns:
            Hash string
        """
        pass

    @abstractmethod
    async def generate_embedding(self, content: str) -> list[float]:
        """Generate embedding for document content.

        Args:
            content: The content to embed

        Returns:
            Embedding vector as list of floats
        """
        pass


class FieldExtractionService(ABC):
    """Abstract service for extracting customs fields."""

    @abstractmethod
    async def extract_fields(
        self, document_text: str, block_category: str
    ) -> list[ExtractedField]:
        """Extract customs fields from document text.

        Args:
            document_text: The text to extract fields from
            block_category: The document category

        Returns:
            List of extracted fields with confidence scores
        """
        pass

    @abstractmethod
    async def validate_field(
        self, field_name: str, field_value: str
    ) -> dict:
        """Validate an extracted field.

        Args:
            field_name: Name of the field
            field_value: Value to validate

        Returns:
            Dictionary with validation results
        """
        pass


class TemplateMappingService(ABC):
    """Abstract service for mapping extracted fields to DUA template."""

    @abstractmethod
    async def find_template_matches(
        self, extracted_text: str, document_category: str, top_k: int = 2
    ) -> list[dict]:
        """Find matching template sections for extracted text.

        Args:
            extracted_text: The text to match
            document_category: The document category for filtering
            top_k: Number of top matches to return

        Returns:
            List of template matches with confidence scores
        """
        pass

    @abstractmethod
    async def map_to_dua_section(
        self, extracted_value: str, candidate_sections: list[dict]
    ) -> dict:
        """Map extracted value to specific DUA section.

        Args:
            extracted_value: The value to map
            candidate_sections: List of candidate DUA sections

        Returns:
            Dictionary with mapping result and confidence
        """
        pass
