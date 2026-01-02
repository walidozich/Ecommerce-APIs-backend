"""Product schema placeholders."""

from datetime import datetime
from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str
    description: str | None = None
    price: float
    category_id: int | None = None


class ProductCreate(ProductBase):
    pass


class ProductRead(ProductBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
