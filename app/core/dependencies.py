"""Shared dependency placeholders."""

from collections.abc import AsyncGenerator
from app.db.session import async_session_factory


async def get_db_session() -> AsyncGenerator:
    async with async_session_factory() as session:
        yield session
