"""API middleware for cross-cutting concerns."""

from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from typing import Callable, Optional
import logging
import uuid

logger = logging.getLogger(__name__)


class AuthenticationMiddleware:
    """Middleware for JWT token validation."""

    def __init__(self, app, auth_port):
        """Initialize authentication middleware.

        Args:
            app: FastAPI application
            auth_port: Authentication port for token validation
        """
        self.app = app
        self.auth_port = auth_port

    async def __call__(self, request: Request, call_next: Callable):
        """Process request for authentication.

        Args:
            request: Incoming request
            call_next: Next middleware/handler

        Returns:
            Response
        """
        # Skip authentication for public endpoints
        if request.url.path in ["/health/live", "/health/ready", "/docs", "/openapi.json"]:
            return await call_next(request)

        auth_header = request.headers.get("Authorization", "")
        if not auth_header.startswith("Bearer "):
            return JSONResponse(
                status_code=401,
                content={"error_code": "MISSING_TOKEN", "message": "Missing or invalid token"}
            )

        token = auth_header.split(" ")[1]
        try:
            # Validate token (stub - implement with auth_port)
            # claims = await self.auth_port.validate_token(token)
            # request.state.user_id = claims.get("sub")
            pass
        except Exception as e:
            return JSONResponse(
                status_code=401,
                content={"error_code": "INVALID_TOKEN", "message": str(e)}
            )

        return await call_next(request)


class RequestLoggingMiddleware:
    """Middleware for structured request/response logging."""

    def __init__(self, app):
        """Initialize logging middleware.

        Args:
            app: FastAPI application
        """
        self.app = app

    async def __call__(self, request: Request, call_next: Callable):
        """Log request and response.

        Args:
            request: Incoming request
            call_next: Next middleware/handler

        Returns:
            Response
        """
        # Generate trace ID if not present
        trace_id = request.headers.get("X-Trace-ID", str(uuid.uuid4()))
        request.state.trace_id = trace_id

        # Log request
        logger.info(
            f"Request: {request.method} {request.url.path}",
            extra={
                "trace_id": trace_id,
                "method": request.method,
                "path": request.url.path,
            }
        )

        response = await call_next(request)

        # Add trace ID to response headers
        response.headers["X-Trace-ID"] = trace_id

        # Log response
        logger.info(
            f"Response: {response.status_code}",
            extra={
                "trace_id": trace_id,
                "status_code": response.status_code,
            }
        )

        return response


class ErrorHandlingMiddleware:
    """Middleware for centralized error handling."""

    def __init__(self, app):
        """Initialize error handling middleware.

        Args:
            app: FastAPI application
        """
        self.app = app

    async def __call__(self, request: Request, call_next: Callable):
        """Handle errors from application.

        Args:
            request: Incoming request
            call_next: Next middleware/handler

        Returns:
            Response
        """
        try:
            response = await call_next(request)
            return response
        except Exception as e:
            trace_id = getattr(request.state, "trace_id", str(uuid.uuid4()))
            logger.error(
                f"Unhandled error: {str(e)}",
                extra={
                    "trace_id": trace_id,
                    "error_type": type(e).__name__,
                }
            )

            return JSONResponse(
                status_code=500,
                content={
                    "error_code": "INTERNAL_ERROR",
                    "message": "An internal error occurred",
                    "trace_id": trace_id,
                }
            )


class RateLimitMiddleware:
    """Middleware for rate limiting."""

    def __init__(self, app, max_concurrent: int = 100):
        """Initialize rate limit middleware.

        Args:
            app: FastAPI application
            max_concurrent: Maximum concurrent requests per user
        """
        self.app = app
        self.max_concurrent = max_concurrent
        self.concurrent_requests = {}

    async def __call__(self, request: Request, call_next: Callable):
        """Apply rate limiting.

        Args:
            request: Incoming request
            call_next: Next middleware/handler

        Returns:
            Response
        """
        # Get user ID from state (set by auth middleware)
        user_id = getattr(request.state, "user_id", "anonymous")

        # Check if user exceeds limit (stub implementation)
        # In production, use external rate limiting service

        response = await call_next(request)
        return response
