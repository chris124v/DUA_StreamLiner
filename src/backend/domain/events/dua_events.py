from dataclasses import dataclass, field
from typing import Optional
from datetime import datetime

from dua_business.domain.events.domain_event import DomainEvent


@dataclass
class UserLoggedInEvent(DomainEvent):
    """Event fired when user successfully authenticates."""

    user_id: str
    auth0_id: str
    timestamp: datetime = field(default_factory=datetime.utcnow)


@dataclass
class UserLoggedOutEvent(DomainEvent):
    """Event fired when user logs out."""

    user_id: str
    timestamp: datetime = field(default_factory=datetime.utcnow)


@dataclass
class DuaGenerationStartedEvent(DomainEvent):
    """Event fired when DUA generation process starts."""

    generation_id: str
    user_id: str
    process_type: str  # import or export
    timestamp: datetime = field(default_factory=datetime.utcnow)


@dataclass
class DocumentsUploadedEvent(DomainEvent):
    """Event fired when documents are uploaded."""

    generation_id: str
    user_id: str
    document_count: int
    timestamp: datetime = field(default_factory=datetime.utcnow)


@dataclass
class DocumentsClassifiedEvent(DomainEvent):
    """Event fired when documents are classified."""

    generation_id: str
    classified_count: int
    timestamp: datetime = field(default_factory=datetime.utcnow)


@dataclass
class OCRProcessedEvent(DomainEvent):
    """Event fired when OCR processing completes."""

    generation_id: str
    document_id: str
    extracted_text_length: int
    timestamp: datetime = field(default_factory=datetime.utcnow)


@dataclass
class FieldsExtractedEvent(DomainEvent):
    """Event fired when fields are extracted from documents."""

    generation_id: str
    extracted_field_count: int
    timestamp: datetime = field(default_factory=datetime.utcnow)


@dataclass
class FieldsMappedEvent(DomainEvent):
    """Event fired when extracted fields are mapped to DUA template."""

    generation_id: str
    mapped_field_count: int
    timestamp: datetime = field(default_factory=datetime.utcnow)


@dataclass
class DuaGeneratedEvent(DomainEvent):
    """Event fired when DUA document is generated."""

    generation_id: str
    user_id: str
    dua_version: str
    timestamp: datetime = field(default_factory=datetime.utcnow)


@dataclass
class GenerationStatusChangedEvent(DomainEvent):
    """Event fired when generation process status changes."""

    generation_id: str
    current_step: int
    percentage_completion: float
    current_task_description: str
    status: str  # PROCESSING, COMPLETED, FAILED
    timestamp: datetime = field(default_factory=datetime.utcnow)


@dataclass
class GenerationFailedEvent(DomainEvent):
    """Event fired when generation process fails."""

    generation_id: str
    step_number: int
    error_message: str
    timestamp: datetime = field(default_factory=datetime.utcnow)


@dataclass
class TemplateBlockHashedEvent(DomainEvent):
    """Event fired when template blocks are hashed and stored."""

    template_version: str
    total_blocks: int
    timestamp: datetime = field(default_factory=datetime.utcnow)
