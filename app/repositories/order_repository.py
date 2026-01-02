"""Order repository placeholder."""

from app.repositories.base import BaseRepository


class OrderRepository(BaseRepository):
    async def list_for_user(self, user_id: int):
        raise NotImplementedError

    async def create(self):
        raise NotImplementedError
