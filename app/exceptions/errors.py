"""Domain-specific exception placeholders."""

class ServiceError(Exception):
    """Base service error."""


class NotFoundError(ServiceError):
    """Raised when a resource is not found."""


class UnauthorizedError(ServiceError):
    """Raised when authentication fails."""
