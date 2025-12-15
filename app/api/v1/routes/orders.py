"""Order routes."""

from fastapi import APIRouter

router = APIRouter()


@router.get("")
async def list_orders() -> dict[str, str]:
    return {"message": "list orders placeholder"}


@router.post("")
async def create_order() -> dict[str, str]:
    return {"message": "create order placeholder"}
