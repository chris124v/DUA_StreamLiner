"""Dependency Injection container for FastAPI."""

from typing import Optional


class Container:
    """IoC Container for dependency injection."""

    def __init__(self):
        """Initialize dependency container."""
        self._services = {}
        self._singletons = {}

    def register_service(self, service_name: str, factory):
        """Register a service factory.

        Args:
            service_name: Name of the service
            factory: Factory function or class
        """
        self._services[service_name] = factory

    def register_singleton(self, service_name: str, instance):
        """Register a singleton instance.

        Args:
            service_name: Name of the service
            instance: Singleton instance
        """
        self._singletons[service_name] = instance

    def get_service(self, service_name: str):
        """Get a service instance.

        Args:
            service_name: Name of the service

        Returns:
            Service instance
        """
        if service_name in self._singletons:
            return self._singletons[service_name]

        if service_name in self._services:
            factory = self._services[service_name]
            return factory()

        raise ValueError(f"Service {service_name} not registered")

    def resolve_all_singletons(self):
        """Resolve all registered services."""
        for service_name, factory in self._services.items():
            if service_name not in self._singletons:
                self._singletons[service_name] = factory()


class AppContainer:
    """Application dependency container."""

    _instance: Optional["AppContainer"] = None

    def __new__(cls):
        """Singleton pattern implementation."""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        """Initialize app container."""
        if self._initialized:
            return

        self.container = Container()
        self._register_services()
        self._initialized = True

    def _register_services(self):
        """Register all application services.

        This is where you wire up all dependencies:
        - Database connections
        - Cache clients
        - External API clients
        - Application services
        - Domain services
        """
        # Stub implementation
        # In production, you would instantiate and register:
        # - Database session factory
        # - Redis connection
        # - Pub/Sub client
        # - GCS client
        # - Auth0 client
        # - Application services
        # - Repositories
        pass

    @staticmethod
    def get_instance() -> "AppContainer":
        """Get container instance.

        Returns:
            Singleton container instance
        """
        return AppContainer()

    def get(self, service_name: str):
        """Get service from container.

        Args:
            service_name: Name of service

        Returns:
            Service instance
        """
        return self.container.get_service(service_name)
