"""Data Transfer Objects for API requests and responses."""

from pydantic import BaseModel, Field
from typing import Optional, list
from datetime import datetime


# Authentication DTOs
class LoginRequestDTO(BaseModel):
    """DTO for login request."""

    jwt_token: str = Field(..., description="JWT token from Auth0")


class LoginResponseDTO(BaseModel):
    """DTO for login response."""

    session_id: str
    user_id: str
    message: str = "Login successful"


class LogoutRequestDTO(BaseModel):
    """DTO for logout request."""

    session_id: str


# DUA Generation DTOs
class CreateDUARequestDTO(BaseModel):
    """DTO for DUA creation request."""

    process_type: str = Field(..., description="'import' or 'export'")
    user_id: str


class DocumentUploadDTO(BaseModel):
    """DTO for document upload."""

    file_name: str
    file_size: int
    file_type: str  # image, excel, word, pdf


class UploadDocumentsRequestDTO(BaseModel):
    """DTO for uploading multiple documents."""

    generation_id: str
    documents: list[DocumentUploadDTO]


# Status and Progress DTOs
class GenerationStatusDTO(BaseModel):
    """DTO for generation status."""

    generation_id: str
    current_step: int
    percentage_completion: float
    current_task_description: str
    status: str  # PROCESSING, COMPLETED, FAILED
    timestamp: datetime


class GenerationProgressDTO(BaseModel):
    """DTO for generation progress update."""

    generation_id: str
    step: int
    progress_percentage: float
    task_description: str
    status: str


# Results DTOs
class ExtractedFieldResultDTO(BaseModel):
    """DTO for extracted field result."""

    field_name: str
    field_value: str
    confidence: float
    warning_level: str  # green, yellow, red
    validation_status: str


class GenerationResultDTO(BaseModel):
    """DTO for generation result."""

    generation_id: str
    template_version: str
    extracted_fields: list[ExtractedFieldResultDTO]
    dua_file_path: str
    completion_timestamp: datetime


class DUADocumentResultDTO(BaseModel):
    """DTO for DUA document result."""

    generation_id: str
    document_id: str
    document_url: str
    fields_count: int
    completion_timestamp: datetime


# Health check DTOs
class HealthStatusDTO(BaseModel):
    """DTO for health check status."""

    status: str  # "healthy", "degraded", "unhealthy"
    timestamp: datetime
    components: dict = Field(default_factory=dict)


class ReadinessStatusDTO(BaseModel):
    """DTO for readiness status."""

    ready: bool
    timestamp: datetime
    checks: dict = Field(default_factory=dict)
