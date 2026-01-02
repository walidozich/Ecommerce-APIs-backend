"""Category schema placeholders."""

from pydantic import BaseModel


class CategoryBase(BaseModel):
    name: str


class CategoryCreate(CategoryBase):
    pass


class CategoryRead(CategoryBase):
    id: int

    class Config:
        from_attributes = True
