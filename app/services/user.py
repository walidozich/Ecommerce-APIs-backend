"""User service placeholder."""

class UserService:
    def __init__(self) -> None:
        pass

    async def list_users(self) -> None:
        raise NotImplementedError

    async def get_user(self, user_id: int) -> None:
        raise NotImplementedError
