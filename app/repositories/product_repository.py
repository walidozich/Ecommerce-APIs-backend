"""Product repository placeholder."""

from app.repositories.base import BaseRepository


class ProductRepository(BaseRepository):
    async def list(self):
        raise NotImplementedError

    async def get(self, product_id: int):
        raise NotImplementedError

    async def create(self):
        raise NotImplementedError
