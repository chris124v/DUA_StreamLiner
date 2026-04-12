"""Shared utilities for the application."""

import uuid
import hashlib
from datetime import datetime, timedelta
from typing import Optional, Any


class IDGenerator:
    """Generator for unique identifiers."""

    @staticmethod
    def generate_id() -> str:
        """Generate a UUID v4 as string.

        Returns:
            UUID string
        """
        return str(uuid.uuid4())

    @staticmethod
    def generate_session_id() -> str:
        """Generate a session ID.

        Returns:
            Session ID
        """
        return f"session_{uuid.uuid4().hex}"

    @staticmethod
    def generate_generation_id() -> str:
        """Generate a DUA generation session ID.

        Returns:
            Generation ID
        """
        return f"gen_{datetime.utcnow().timestamp()}_{uuid.uuid4().hex}"


class HashingUtil:
    """Utility for hashing operations."""

    @staticmethod
    def hash_content(content: str, algorithm: str = "sha256") -> str:
        """Hash content using specified algorithm.

        Args:
            content: Content to hash
            algorithm: Hashing algorithm (sha256, sha512, md5)

        Returns:
            Hex digest of hash
        """
        if algorithm == "sha256":
            return hashlib.sha256(content.encode()).hexdigest()
        elif algorithm == "sha512":
            return hashlib.sha512(content.encode()).hexdigest()
        elif algorithm == "md5":
            return hashlib.md5(content.encode()).hexdigest()
        else:
            raise ValueError(f"Unsupported algorithm: {algorithm}")

    @staticmethod
    def calculate_file_hash(file_bytes: bytes, algorithm: str = "sha256") -> str:
        """Calculate hash of file content.

        Args:
            file_bytes: File content as bytes
            algorithm: Hashing algorithm

        Returns:
            Hex digest of hash
        """
        if algorithm == "sha256":
            return hashlib.sha256(file_bytes).hexdigest()
        elif algorithm == "sha512":
            return hashlib.sha512(file_bytes).hexdigest()
        elif algorithm == "md5":
            return hashlib.md5(file_bytes).hexdigest()
        else:
            raise ValueError(f"Unsupported algorithm: {algorithm}")


class DateTimeUtil:
    """Utility for datetime operations."""

    @staticmethod
    def get_utc_now() -> datetime:
        """Get current UTC datetime.

        Returns:
            Current datetime in UTC
        """
        return datetime.utcnow()

    @staticmethod
    def add_hours(dt: datetime, hours: int) -> datetime:
        """Add hours to a datetime.

        Args:
            dt: Base datetime
            hours: Hours to add

        Returns:
            New datetime
        """
        return dt + timedelta(hours=hours)

    @staticmethod
    def add_days(dt: datetime, days: int) -> datetime:
        """Add days to a datetime.

        Args:
            dt: Base datetime
            days: Days to add

        Returns:
            New datetime
        """
        return dt + timedelta(days=days)

    @staticmethod
    def is_expired(dt: datetime, ttl_seconds: int) -> bool:
        """Check if datetime has expired.

        Args:
            dt: DateTime to check
            ttl_seconds: Time to live in seconds

        Returns:
            True if expired, False otherwise
        """
        expiration = dt + timedelta(seconds=ttl_seconds)
        return datetime.utcnow() > expiration


class ValidationUtil:
    """Utility for validation operations."""

    @staticmethod
    def is_valid_email(email: str) -> bool:
        """Validate email format.

        Args:
            email: Email address

        Returns:
            True if valid email format
        """
        import re
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return re.match(pattern, email) is not None

    @staticmethod
    def is_valid_iso_date(date_string: str) -> bool:
        """Validate ISO 8601 date format.

        Args:
            date_string: Date string

        Returns:
            True if valid ISO date
        """
        try:
            datetime.fromisoformat(date_string)
            return True
        except (ValueError, TypeError):
            return False

    @staticmethod
    def is_valid_country_code(code: str) -> bool:
        """Validate ISO 3166-1 alpha-3 country code.

        Args:
            code: Country code

        Returns:
            True if valid country code
        """
        valid_codes = [
            "CRI", "USA", "MEX", "ESP", "DEU", "FRA", "GBR", "CHN", "JPN", "IND",
            # Add more as needed or use external library
        ]
        return code.upper() in valid_codes

    @staticmethod
    def is_valid_currency_code(code: str) -> bool:
        """Validate ISO 4217 currency code.

        Args:
            code: Currency code

        Returns:
            True if valid currency code
        """
        valid_codes = [
            "USD", "EUR", "GBP", "JPY", "CNY", "CRC", "MXN",  # Common codes
            # Add more as needed
        ]
        return code.upper() in valid_codes
