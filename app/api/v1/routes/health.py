"""Health check route."""

from fastapi import APIRouter

router = APIRouter()


@router.get("", summary="Health status")
async def health() -> dict[str, str]:
    return {"status": "ok"}
