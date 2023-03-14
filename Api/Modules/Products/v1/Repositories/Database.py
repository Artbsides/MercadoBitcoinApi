from uuid import UUID
from fastapi import Depends
from sqlalchemy.orm import Session
from Api.Confs.Database import getDatabase
from Api.Modules.Products.v1.Models.Product import Product


class ProductsDatabaseRepository:
    def __init__(self, database: Session = Depends(getDatabase)) -> None:
        self.database = database

    def create(self, product: Product) -> None:
        self.database.add(product)

    def getAll(self) -> list[Product]:
        return self.database.query(Product).all()

    def get(self, product_id: UUID) -> Product:
        return self.database.query(Product).get(product_id)

    def update(self, product: Product) -> Product:
        try:
            return self.database.query(Product) \
                .filter(Product.id == product.id).update(product.toDict())
        finally:
            pass

    def delete(self, product_id: UUID) -> int:
        try:
            return self.database.query(Product) \
                .filter(Product.id == product_id).delete()
        finally:
            pass
