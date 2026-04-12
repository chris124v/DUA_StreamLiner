"""Structured logging for observability."""

import logging
import json
from datetime import datetime
from typing import Any, Optional
from pythonjsonlogger import jsonlogger


class StructuredLogger:
    """Structured JSON logger for Cloud Logging integration."""

    def __init__(self, name: str):
        """Initialize structured logger.

        Args:
            name: Logger name
        """
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)

        # Add JSON formatter
        if not self.logger.handlers:
            handler = logging.StreamHandler()
            formatter = jsonlogger.JsonFormatter()
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)

    def log(
        self,
        level: str,
        message: str,
        trace_id: Optional[str] = None,
        request_id: Optional[str] = None,
        user_id: Optional[str] = None,
        user_role: Optional[str] = None,
        endpoint: Optional[str] = None,
        method: Optional[str] = None,
        status_code: Optional[int] = None,
        extra: Optional[dict] = None,
    ) -> None:
        """Log structured event.

        Args:
            level: Log level (INFO, WARNING, ERROR, etc.)
            message: Log message
            trace_id: X-Trace-ID for request correlation
            request_id: Request ID
            user_id: User ID
            user_role: User role
            endpoint: API endpoint
            method: HTTP method
            status_code: HTTP status code
            extra: Additional fields
        """
        log_data = {
            "timestamp": datetime.utcnow().isoformat(),
            "level": level,
            "message": message,
            "service": "dua-business",
            "environment": self._get_environment(),
            "version": "0.1.0",
        }

        if trace_id:
            log_data["trace_id"] = trace_id
        if request_id:
            log_data["request_id"] = request_id
        if user_id:
            log_data["user_id"] = user_id
        if user_role:
            log_data["user_role"] = user_role
        if endpoint:
            log_data["endpoint"] = endpoint
        if method:
            log_data["method"] = method
        if status_code:
            log_data["status_code"] = status_code

        if extra:
            log_data.update(extra)

        log_level = getattr(logging, level.upper(), logging.INFO)
        self.logger.log(log_level, json.dumps(log_data))

    def info(self, message: str, **kwargs) -> None:
        """Log info level."""
        self.log("INFO", message, **kwargs)

    def warning(self, message: str, **kwargs) -> None:
        """Log warning level."""
        self.log("WARNING", message, **kwargs)

    def error(self, message: str, **kwargs) -> None:
        """Log error level."""
        self.log("ERROR", message, **kwargs)

    def debug(self, message: str, **kwargs) -> None:
        """Log debug level."""
        self.log("DEBUG", message, **kwargs)

    @staticmethod
    def _get_environment() -> str:
        """Get current environment."""
        import os
        return os.getenv("ENVIRONMENT", "development")
