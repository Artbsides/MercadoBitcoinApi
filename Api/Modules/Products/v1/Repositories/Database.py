from fastapi import Depends
from pytest import Session

from Api.Confs.Database import getDatabase
from Api.Modules.Products.v1.Models.Product import Product


class ProductsDatabaseRepository:
    def __init__(self, database: Session = Depends(getDatabase)) -> None:
        self.database = database

    def get(self, product_id: str) -> Product:
        return self.database.query(Product).get(product_id)

    def getAll(self) -> list[Product]:
        return self.database.query(Product).all()

    def create(self, product: Product) -> Product:
        self.database.add(product)
        self.database.commit()

        return product
