"""Authentication service placeholder."""

class AuthService:
    def __init__(self) -> None:
        pass

    async def login(self) -> None:
        raise NotImplementedError

    async def refresh(self) -> None:
        raise NotImplementedError

    async def register(self) -> None:
        raise NotImplementedError
