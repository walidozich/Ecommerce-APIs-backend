"""Order schema placeholders."""

from datetime import datetime
from pydantic import BaseModel


class OrderItem(BaseModel):
    product_id: int
    price: float
    quantity: int


class OrderCreate(BaseModel):
    items: list[OrderItem]


class OrderRead(BaseModel):
    id: int
    user_id: int
    total_amount: float
    status: str
    created_at: datetime
    items: list[OrderItem] = []

    class Config:
        from_attributes = True
