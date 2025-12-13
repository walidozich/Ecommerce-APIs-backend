"""Exception handler placeholders."""

from fastapi import Request
from fastapi.responses import JSONResponse
from app.exceptions.errors import ServiceError


async def service_error_handler(_: Request, exc: ServiceError) -> JSONResponse:
    return JSONResponse(status_code=400, content={"detail": str(exc)})
