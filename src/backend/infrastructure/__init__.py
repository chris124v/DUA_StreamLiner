"""Infrastructure layer."""

from dua_business.infrastructure.ai.vertex_ai_adapter import VertexAIAdapter
from dua_business.infrastructure.auth.auth0_adapter import Auth0JWTAdapter
from dua_business.infrastructure.ocr.document_ai_adapter import DocumentAIOCRAdapter
from dua_business.infrastructure.storage.gcs_storage_adapter import GCSStorageAdapter
from dua_business.infrastructure.persistence.redis.redis_cache_adapter import RedisSessionCacheAdapter
from dua_business.infrastructure.messaging.pubsub_adapter import PubSubMessageBusAdapter
from dua_business.infrastructure.tasks.cloud_tasks_adapter import CloudTasksAdapter
from dua_business.infrastructure.persistence.cloudsql.repositories import (
    UserRepository,
    DUAGenerationRepository,
    DocumentRepository,
)
from dua_business.infrastructure.config.settings import settings

__all__ = [
    "VertexAIAdapter",
    "Auth0JWTAdapter",
    "DocumentAIOCRAdapter",
    "GCSStorageAdapter",
    "RedisSessionCacheAdapter",
    "PubSubMessageBusAdapter",
    "CloudTasksAdapter",
    "UserRepository",
    "DUAGenerationRepository",
    "DocumentRepository",
    "settings",
]
