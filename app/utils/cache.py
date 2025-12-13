"""Redis cache helper placeholders."""

from redis.asyncio import Redis


class Cache:
    def __init__(self, client: Redis) -> None:
        self.client = client

    async def get(self, key: str):
        raise NotImplementedError

    async def set(self, key: str, value: str, ttl: int | None = None):
        raise NotImplementedError
