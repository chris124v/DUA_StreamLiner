"""Mappers for converting between DTOs and domain models."""

from abc import ABC, abstractmethod
from typing import Optional
from dua_business.domain.entities import User, DUAGeneration, Document


class UserMapper(ABC):
    """Mapper for User entity and DTOs."""

    @staticmethod
    @abstractmethod
    def to_domain(auth_claims: dict) -> User:
        """Convert auth claims to domain User entity.

        Args:
            auth_claims: JWT token claims from Auth0

        Returns:
            User domain entity
        """
        pass

    @staticmethod
    @abstractmethod
    def to_dto(user: User) -> dict:
        """Convert domain User to DTO.

        Args:
            user: Domain User entity

        Returns:
            User DTO dictionary
        """
        pass


class DUAGenerationMapper(ABC):
    """Mapper for DUA generation and related objects."""

    @staticmethod
    @abstractmethod
    def to_domain(generation_data: dict) -> DUAGeneration:
        """Convert generation data to domain entity.

        Args:
            generation_data: Generation data dictionary

        Returns:
            DUAGeneration domain entity
        """
        pass

    @staticmethod
    @abstractmethod
    def to_dto(generation: DUAGeneration) -> dict:
        """Convert domain generation to DTO.

        Args:
            generation: Domain DUAGeneration entity

        Returns:
            Generation DTO dictionary
        """
        pass


class DocumentMapper(ABC):
    """Mapper for Document entity and DTOs."""

    @staticmethod
    @abstractmethod
    def to_domain(document_data: dict) -> Document:
        """Convert document data to domain entity.

        Args:
            document_data: Document data dictionary

        Returns:
            Document domain entity
        """
        pass

    @staticmethod
    @abstractmethod
    def to_dto(document: Document) -> dict:
        """Convert domain document to DTO.

        Args:
            document: Domain Document entity

        Returns:
            Document DTO dictionary
        """
        pass


class ExternalAPIResponseMapper(ABC):
    """Mapper for converting external API responses to domain objects."""

    @staticmethod
    @abstractmethod
    def map_vertex_ai_response(response: dict) -> dict:
        """Map Vertex AI API response to domain format.

        Args:
            response: Raw Vertex AI API response

        Returns:
            Mapped response dictionary
        """
        pass

    @staticmethod
    @abstractmethod
    def map_ocr_response(response: dict) -> dict:
        """Map OCR service response to domain format.

        Args:
            response: Raw OCR service response

        Returns:
            Mapped OCR results
        """
        pass
