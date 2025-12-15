"""Admin routes."""

from fastapi import APIRouter

router = APIRouter()


@router.get("/dashboard")
async def dashboard() -> dict[str, str]:
    return {"message": "admin dashboard placeholder"}
