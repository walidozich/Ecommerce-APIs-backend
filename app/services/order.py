"""Order service placeholder."""

class OrderService:
    def __init__(self) -> None:
        pass

    async def list_orders(self, user_id: int) -> None:
        raise NotImplementedError

    async def create_order(self, user_id: int) -> None:
        raise NotImplementedError
