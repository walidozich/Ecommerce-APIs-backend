"""Cart repository placeholder."""

from app.repositories.base import BaseRepository


class CartRepository(BaseRepository):
    async def get_for_user(self, user_id: int):
        raise NotImplementedError

    async def add_item(self, user_id: int):
        raise NotImplementedError

    async def remove_item(self, user_id: int, item_id: int):
        raise NotImplementedError
