"""Category routes."""

from fastapi import APIRouter

router = APIRouter()


@router.get("")
async def list_categories() -> dict[str, str]:
    return {"message": "list categories placeholder"}


@router.post("")
async def create_category() -> dict[str, str]:
    return {"message": "create category placeholder"}
