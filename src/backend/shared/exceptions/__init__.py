"""Application exceptions."""

from dua_business.shared.exceptions.app_exception import (
    AppException,
    AuthenticationException,
    AuthorizationException,
    ValidationException,
    ResourceNotFoundException,
    ConflictException,
    GenerationException,
    DocumentProcessingException,
    OCRException,
    ExtractionException,
    StorageException,
    ExternalServiceException,
    SessionException,
)

__all__ = [
    "AppException",
    "AuthenticationException",
    "AuthorizationException",
    "ValidationException",
    "ResourceNotFoundException",
    "ConflictException",
    "GenerationException",
    "DocumentProcessingException",
    "OCRException",
    "ExtractionException",
    "StorageException",
    "ExternalServiceException",
    "SessionException",
]
