"""Product routes."""

from fastapi import APIRouter

router = APIRouter()


@router.get("")
async def list_products() -> dict[str, str]:
    return {"message": "list products placeholder"}


@router.get("/{product_id}")
async def get_product(product_id: int) -> dict[str, int | str]:
    return {"message": "get product placeholder", "product_id": product_id}


@router.post("")
async def create_product() -> dict[str, str]:
    return {"message": "create product placeholder"}
