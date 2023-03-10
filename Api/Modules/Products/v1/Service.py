from uuid import UUID
from fastapi import Depends
from Api.Modules.Products.v1.Models.Product import Product
from Api.Modules.Products.v1.Repositories.Database import ProductsDatabaseRepository


class ProductsService:
    def __init__(self, productsDatabaseRepository: ProductsDatabaseRepository = Depends()) -> None:
        self.productsDatabaseRepository = productsDatabaseRepository

    def create(self, product: Product) -> Product:
        return self.productsDatabaseRepository.create(product)

    def getAll(self) -> list[Product]:
        return self.productsDatabaseRepository.getAll()

    def get(self, product_id: UUID) -> Product:
        return self.productsDatabaseRepository.get(product_id)

    def update(self, product: Product) -> Product:
        return self.productsDatabaseRepository.update(product)

    def delete(self, product_id: UUID) -> Product:
        return self.productsDatabaseRepository.update(product_id)
