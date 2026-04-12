"""DUA StreamLiner Backend - Domain-Driven Design based REST API."""

__version__ = "0.1.0"
__author__ = "Isaac Villalobos, Christopher Vargas"
__description__ = "Automated DUA document generation and processing system"

from dua_business import domain, application, infrastructure, api, shared, workers

__all__ = [
    "domain",
    "application",
    "infrastructure",
    "api",
    "shared",
    "workers",
]
