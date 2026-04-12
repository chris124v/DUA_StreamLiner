"""API request/response schemas for validation."""

from pydantic import BaseModel, Field, validator
from typing import Optional, List
from datetime import datetime


# Request Schemas
class LoginRequest(BaseModel):
    """Login request schema."""

    jwt_token: str = Field(..., description="JWT token from Auth0")


class CreateDUARequest(BaseModel):
    """Create DUA generation request."""

    process_type: str = Field(..., description="'import' or 'export'")

    @validator("process_type")
    def validate_process_type(cls, v):
        if v not in ["import", "export"]:
            raise ValueError("process_type must be 'import' or 'export'")
        return v


class UploadDocumentsRequest(BaseModel):
    """Upload documents request."""

    generation_id: str = Field(..., description="Generation session ID")
    file_names: List[str] = Field(..., description="List of file names")


class LogoutRequest(BaseModel):
    """Logout request."""

    pass  # Requires valid session token


class UpdateDUAFieldsRequest(BaseModel):
    """Update DUA fields request."""

    generation_id: str = Field(..., description="Generation session ID")
    field_mappings: dict = Field(..., description="Field name to value mappings")


# Response Schemas
class LoginResponse(BaseModel):
    """Login response schema."""

    session_id: str
    user_id: str
    message: str


class ErrorResponse(BaseModel):
    """Error response schema."""

    error_code: str
    message: str
    details: Optional[dict] = None
    timestamp: datetime


class GenerationStatusResponse(BaseModel):
    """Generation status response."""

    generation_id: str
    current_step: int
    percentage_completion: float
    current_task_description: str
    status: str
    timestamp: datetime


class ExtractedFieldResponse(BaseModel):
    """Extracted field response."""

    field_name: str
    field_value: str
    confidence: float
    warning_level: str


class GenerationResultResponse(BaseModel):
    """Generation result response."""

    generation_id: str
    template_version: str
    extracted_fields: List[ExtractedFieldResponse]
    dua_file_path: str
    completion_timestamp: datetime


class HealthResponse(BaseModel):
    """Health check response."""

    status: str
    timestamp: datetime
    components: dict


class PaginationMetadata(BaseModel):
    """Pagination metadata."""

    page: int
    page_size: int
    total_count: int
    total_pages: int


class ListGenerationsResponse(BaseModel):
    """List generations response."""

    data: List[GenerationStatusResponse]
    pagination: PaginationMetadata
