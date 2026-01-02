"""User repository placeholder."""

from app.repositories.base import BaseRepository


class UserRepository(BaseRepository):
    async def list(self):
        raise NotImplementedError

    async def get(self, user_id: int):
        raise NotImplementedError
