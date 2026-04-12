"""Application configuration from environment variables."""

import os
from typing import Optional


class Settings:
    """Application settings from environment."""

    # GCP Configuration
    GCP_PROJECT_ID: str = os.getenv("GCP_PROJECT_ID", "")
    GCP_REGION: str = os.getenv("GCP_REGION", "us-central1")

    # Database Configuration
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL", "postgresql://user:password@localhost/duabusiness"
    )
    DATABASE_POOL_SIZE: int = int(os.getenv("DATABASE_POOL_SIZE", "10"))

    # Redis Configuration
    REDIS_URL: str = os.getenv("REDIS_URL", "redis://localhost:6379")
    REDIS_TTL: int = int(os.getenv("REDIS_TTL", "3600"))

    # Auth0 Configuration
    AUTH0_DOMAIN: str = os.getenv("AUTH0_DOMAIN", "")
    AUTH0_CLIENT_ID: str = os.getenv("AUTH0_CLIENT_ID", "")
    AUTH0_CLIENT_SECRET: str = os.getenv("AUTH0_CLIENT_SECRET", "")
    AUTH0_AUDIENCE: str = os.getenv("AUTH0_AUDIENCE", "")

    # GCS Configuration
    GCS_BUCKET_NAME: str = os.getenv("GCS_BUCKET_NAME", "dua-documents")
    GCS_TEMP_BUCKET: str = os.getenv("GCS_TEMP_BUCKET", "dua-temp")

    # Pub/Sub Configuration
    PUBSUB_TOPIC_DUA_PROCESSING: str = os.getenv(
        "PUBSUB_TOPIC_DUA_PROCESSING", "dua-processing"
    )
    PUBSUB_SUBSCRIPTION_DUA: str = os.getenv(
        "PUBSUB_SUBSCRIPTION_DUA", "dua-processing-sub"
    )

    # Cloud Tasks Configuration
    CLOUD_TASKS_QUEUE: str = os.getenv("CLOUD_TASKS_QUEUE", "dua-processing-queue")
    CLOUD_TASKS_LOCATION: str = os.getenv("CLOUD_TASKS_LOCATION", "us-central1")

    # Vertex AI Configuration
    VERTEX_AI_LOCATION: str = os.getenv("VERTEX_AI_LOCATION", "us-central1")
    VERTEX_AI_EMBEDDING_MODEL: str = os.getenv(
        "VERTEX_AI_EMBEDDING_MODEL", "textembedding-gecko@001"
    )
    VERTEX_AI_LLM_MODEL: str = os.getenv(
        "VERTEX_AI_LLM_MODEL", "gemini-1.5-pro"
    )

    # Document AI Configuration
    DOCUMENT_AI_LOCATION: str = os.getenv("DOCUMENT_AI_LOCATION", "us")
    DOCUMENT_AI_PROCESSOR_ID: str = os.getenv("DOCUMENT_AI_PROCESSOR_ID", "")

    # Application Configuration
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
    DEBUG: bool = os.getenv("DEBUG", "false").lower() == "true"
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    API_TITLE: str = "DUA StreamLiner API"
    API_VERSION: str = "0.1.0"
    MAX_CONCURRENT_REQUESTS: int = int(os.getenv("MAX_CONCURRENT_REQUESTS", "100"))
    MAX_UPLOAD_SIZE_MB: int = int(os.getenv("MAX_UPLOAD_SIZE_MB", "50"))

    # Feature Flags
    ENABLE_OCR: bool = os.getenv("ENABLE_OCR", "true").lower() == "true"
    ENABLE_AI_EXTRACTION: bool = os.getenv("ENABLE_AI_EXTRACTION", "true").lower() == "true"
    ENABLE_TEMPLATE_CACHING: bool = os.getenv("ENABLE_TEMPLATE_CACHING", "true").lower() == "true"

    @property
    def is_production(self) -> bool:
        """Check if running in production."""
        return self.ENVIRONMENT == "production"

    @property
    def is_development(self) -> bool:
        """Check if running in development."""
        return self.ENVIRONMENT == "development"


settings = Settings()
