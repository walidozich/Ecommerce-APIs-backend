"""Async database session factory placeholder."""

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession
from app.core.config import settings

engine = create_async_engine(settings.database_url, echo=False, future=True)
async_session_factory = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
