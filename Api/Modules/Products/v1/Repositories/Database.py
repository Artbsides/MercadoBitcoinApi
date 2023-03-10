from uuid import UUID
from fastapi import Depends
from sqlalchemy.orm import Session
from Api.Confs.Database import getDatabase
from Api.Modules.Products.v1.Models.Product import Product


class ProductsDatabaseRepository:
    def __init__(self, database: Session = Depends(getDatabase)) -> None:
        self.database = database

    def create(self, product: Product) -> Product:
        self.database.add(product)
        self.database.commit()

        return product

    def getAll(self) -> list[Product]:
        return self.database.query(Product).all()

    def get(self, product_id: UUID) -> Product:
        return self.database.query(Product).get(product_id)

    def update(self, product: Product) -> Product:
        return self.database.query(Product).update(product)

    def delete(self, product_id: UUID) -> Product:
        return self.database.query(Product).delete(product_id)
