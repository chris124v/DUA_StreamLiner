"""Application exceptions."""

from typing import Optional


class AppException(Exception):
    """Base application exception."""

    def __init__(self, message: str, code: str = "INTERNAL_ERROR", details: Optional[dict] = None):
        """Initialize app exception.

        Args:
            message: Error message
            code: Error code for API response
            details: Additional error details
        """
        self.message = message
        self.code = code
        self.details = details or {}
        super().__init__(self.message)


class AuthenticationException(AppException):
    """Raised when authentication fails."""

    def __init__(self, message: str = "Authentication failed", details: Optional[dict] = None):
        super().__init__(message, "AUTHENTICATION_ERROR", details)


class AuthorizationException(AppException):
    """Raised when user lacks permission."""

    def __init__(self, message: str = "Not authorized", details: Optional[dict] = None):
        super().__init__(message, "AUTHORIZATION_ERROR", details)


class ValidationException(AppException):
    """Raised when input validation fails."""

    def __init__(self, message: str = "Validation failed", details: Optional[dict] = None):
        super().__init__(message, "VALIDATION_ERROR", details)


class ResourceNotFoundException(AppException):
    """Raised when resource not found."""

    def __init__(self, resource_type: str, resource_id: str):
        message = f"{resource_type} with ID {resource_id} not found"
        super().__init__(message, "NOT_FOUND")


class ConflictException(AppException):
    """Raised on resource conflict."""

    def __init__(self, message: str, details: Optional[dict] = None):
        super().__init__(message, "CONFLICT", details)


class GenerationException(AppException):
    """Raised when DUA generation fails."""

    def __init__(self, message: str = "DUA generation failed", step: Optional[int] = None, details: Optional[dict] = None):
        if step:
            message = f"DUA generation failed at step {step}: {message}"
        super().__init__(message, "GENERATION_FAILED", details)


class DocumentProcessingException(AppException):
    """Raised when document processing fails."""

    def __init__(self, message: str = "Document processing failed", document_id: Optional[str] = None, details: Optional[dict] = None):
        if document_id:
            message = f"Failed to process document {document_id}: {message}"
        super().__init__(message, "DOCUMENT_PROCESSING_ERROR", details)


class OCRException(AppException):
    """Raised when OCR processing fails."""

    def __init__(self, message: str = "OCR processing failed", details: Optional[dict] = None):
        super().__init__(message, "OCR_ERROR", details)


class ExtractionException(AppException):
    """Raised when field extraction fails."""

    def __init__(self, message: str = "Field extraction failed", details: Optional[dict] = None):
        super().__init__(message, "EXTRACTION_ERROR", details)


class StorageException(AppException):
    """Raised when storage operations fail."""

    def __init__(self, message: str = "Storage operation failed", details: Optional[dict] = None):
        super().__init__(message, "STORAGE_ERROR", details)


class ExternalServiceException(AppException):
    """Raised when external service calls fail."""

    def __init__(self, service_name: str, message: str = "External service error", details: Optional[dict] = None):
        message = f"{service_name} error: {message}"
        super().__init__(message, "EXTERNAL_SERVICE_ERROR", details)


class SessionException(AppException):
    """Raised when session operations fail."""

    def __init__(self, message: str = "Session error", details: Optional[dict] = None):
        super().__init__(message, "SESSION_ERROR", details)
