"""Authentication routes."""

from fastapi import APIRouter

router = APIRouter()


@router.post("/login")
async def login() -> dict[str, str]:
    return {"message": "login placeholder"}


@router.post("/refresh")
async def refresh() -> dict[str, str]:
    return {"message": "refresh placeholder"}


@router.post("/register")
async def register() -> dict[str, str]:
    return {"message": "register placeholder"}
