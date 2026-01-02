"""User schema placeholders."""

from datetime import datetime
from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    password: str


class UserRead(UserBase):
    id: int
    role: str
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True
