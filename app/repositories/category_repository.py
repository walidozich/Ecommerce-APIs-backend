"""Category repository placeholder."""

from app.repositories.base import BaseRepository


class CategoryRepository(BaseRepository):
    async def list(self):
        raise NotImplementedError

    async def create(self):
        raise NotImplementedError
