"""User routes."""

from fastapi import APIRouter

router = APIRouter()


@router.get("")
async def list_users() -> dict[str, str]:
    return {"message": "list users placeholder"}


@router.get("/{user_id}")
async def get_user(user_id: int) -> dict[str, int | str]:
    return {"message": "get user placeholder", "user_id": user_id}
