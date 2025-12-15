"""Cart routes."""

from fastapi import APIRouter

router = APIRouter()


@router.get("")
async def get_cart() -> dict[str, str]:
    return {"message": "get cart placeholder"}


@router.post("/items")
async def add_item() -> dict[str, str]:
    return {"message": "add cart item placeholder"}


@router.delete("/items/{item_id}")
async def remove_item(item_id: int) -> dict[str, int | str]:
    return {"message": "remove cart item placeholder", "item_id": item_id}
