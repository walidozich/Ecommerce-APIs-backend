"""Cart service placeholder."""

class CartService:
    def __init__(self) -> None:
        pass

    async def get_cart(self, user_id: int) -> None:
        raise NotImplementedError

    async def add_item(self, user_id: int) -> None:
        raise NotImplementedError

    async def remove_item(self, user_id: int, item_id: int) -> None:
        raise NotImplementedError
