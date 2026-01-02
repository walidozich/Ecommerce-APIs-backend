"""Cart schema placeholders."""

from pydantic import BaseModel


class CartItem(BaseModel):
    product_id: int
    quantity: int


class Cart(BaseModel):
    id: int
    user_id: int
    items: list[CartItem] = []

    class Config:
        from_attributes = True
