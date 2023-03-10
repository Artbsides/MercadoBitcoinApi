from uuid import UUID
from fastapi import Depends
from Api.Modules.Products.v1.Models.Product import Product
from Api.Modules.Products.v1.Repositories.Cache import ProductsCacheRepository
from Api.Modules.Products.v1.Repositories.Database import ProductsDatabaseRepository


class ProductsService:
    def __init__(
        self,
        productsCacheRepository: ProductsCacheRepository = Depends(),
        productsDatabaseRepository: ProductsDatabaseRepository = Depends()
    ) -> None:
        self.productsCacheRepository = productsCacheRepository
        self.productsDatabaseRepository = productsDatabaseRepository

    def create(self, product: Product) -> Product:
        self.productsDatabaseRepository \
            .create(product)

        self.productsCacheRepository.create(product)

        return product

    def getAll(self) -> list[Product]:
        return self.productsDatabaseRepository.getAll()

    def get(self, product_id: UUID) -> Product:
        return self.productsCacheRepository.get(product_id) or \
            self.productsDatabaseRepository.get(product_id)

    def update(self, product: Product) -> Product:
        return self.productsDatabaseRepository.update(product)

    def delete(self, product_id: UUID) -> Product:
        return self.productsDatabaseRepository.update(product_id)
