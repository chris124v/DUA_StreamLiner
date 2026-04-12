"""SQLAlchemy models for Cloud SQL (PostgreSQL) database."""

from sqlalchemy import Column, String, DateTime, Integer, Float, JSON, ForeignKey, Boolean, Enum, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime
import enum

Base = declarative_base()


class UserModel(Base):
    """User entity model."""

    __tablename__ = "users"

    id = Column(String(36), primary_key=True)
    auth0_id = Column(String(255), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    name = Column(String(255), nullable=True)
    role = Column(String(50), nullable=False)  # 'manager', 'customs_agent'
    permissions = Column(JSON, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    generations = relationship("DUAGenerationModel", back_populates="user")


class DUAGenerationModel(Base):
    """DUA Generation session model."""

    __tablename__ = "dua_generations"

    id = Column(String(36), primary_key=True)
    user_id = Column(String(36), ForeignKey("users.id"), nullable=False)
    process_type = Column(String(20), nullable=False)  # 'import', 'export'
    template_version = Column(String(50), nullable=False)
    status = Column(String(50), nullable=False)  # 'processing', 'completed', 'failed'
    current_step = Column(Integer, nullable=False, default=0)
    percentage_completion = Column(Float, nullable=False, default=0.0)
    current_task_description = Column(String(500), nullable=True)
    error_message = Column(Text, nullable=True)
    result_file_path = Column(String(500), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    completed_at = Column(DateTime, nullable=True)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = relationship("UserModel", back_populates="generations")
    documents = relationship("DocumentModel", back_populates="generation")
    field_mappings = relationship("FieldMappingModel", back_populates="generation")


class DocumentModel(Base):
    """Document entity model."""

    __tablename__ = "documents"

    id = Column(String(36), primary_key=True)
    generation_id = Column(String(36), ForeignKey("dua_generations.id"), nullable=False)
    file_name = Column(String(500), nullable=False)
    file_type = Column(String(20), nullable=False)  # 'image', 'excel', 'word', 'pdf'
    storage_path = Column(String(500), nullable=False)
    file_size = Column(Integer, nullable=False)
    document_category = Column(String(50), nullable=True)  # 'commercial_invoice', etc.
    category_confidence_scores = Column(JSON, nullable=True)
    extracted_text = Column(Text, nullable=True)
    block_hash = Column(String(255), nullable=True)
    embedding_vector = Column(JSON, nullable=True)  # Stored as JSON for simplicity
    layout_info = Column(JSON, nullable=True)
    processing_status = Column(String(50), nullable=False)  # 'pending', 'processing', 'completed', 'failed'
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    generation = relationship("DUAGenerationModel", back_populates="documents")
    extracted_fields = relationship("ExtractedFieldModel", back_populates="document")


class ExtractedFieldModel(Base):
    """Extracted field model."""

    __tablename__ = "extracted_fields"

    id = Column(String(36), primary_key=True)
    document_id = Column(String(36), ForeignKey("documents.id"), nullable=False)
    field_name = Column(String(255), nullable=False)
    field_value = Column(Text, nullable=False)
    confidence = Column(Float, nullable=False)
    validation_status = Column(String(50), nullable=False)  # 'valid', 'invalid', 'requires_review'
    validation_details = Column(JSON, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    document = relationship("DocumentModel", back_populates="extracted_fields")


class FieldMappingModel(Base):
    """Field mapping to DUA template model."""

    __tablename__ = "field_mappings"

    id = Column(String(36), primary_key=True)
    generation_id = Column(String(36), ForeignKey("dua_generations.id"), nullable=False)
    dua_section = Column(String(255), nullable=False)
    dua_field_name = Column(String(255), nullable=False)
    extracted_value = Column(Text, nullable=False)
    confidence_score = Column(Float, nullable=False)
    warning_level = Column(String(20), nullable=False)  # 'green', 'yellow', 'red'
    alternative_matches = Column(JSON, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    generation = relationship("DUAGenerationModel", back_populates="field_mappings")


class DocumentBlockModel(Base):
    """Document block with embedding model."""

    __tablename__ = "document_blocks"

    id = Column(String(36), primary_key=True)
    document_id = Column(String(36), ForeignKey("documents.id"), nullable=True)
    content = Column(Text, nullable=False)
    block_hash = Column(String(255), nullable=False, unique=True)
    embedding_vector = Column(JSON, nullable=False)  # 512-dim vector
    document_category = Column(String(50), nullable=False)
    file_type = Column(String(20), nullable=False)
    confidence_scores = Column(JSON, nullable=False)
    top_categories = Column(JSON, nullable=False)
    layout_info = Column(JSON, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)


class DUATemplateModel(Base):
    """DUA template model."""

    __tablename__ = "dua_templates"

    id = Column(String(36), primary_key=True)
    version = Column(String(50), nullable=False, unique=True)
    process_type = Column(String(20), nullable=False)  # 'import', 'export'
    template_hash = Column(String(255), nullable=False)
    template_content = Column(JSON, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
