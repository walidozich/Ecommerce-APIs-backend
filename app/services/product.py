"""Product service placeholder."""

class ProductService:
    def __init__(self) -> None:
        pass

    async def list_products(self) -> None:
        raise NotImplementedError

    async def get_product(self, product_id: int) -> None:
        raise NotImplementedError

    async def create_product(self) -> None:
        raise NotImplementedError
