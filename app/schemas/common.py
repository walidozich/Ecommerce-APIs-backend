"""Common schema primitives."""

from pydantic import BaseModel


class Message(BaseModel):
    message: str
