from uuid import UUID
from fastapi import Depends
from sqlalchemy.orm import Session
from Api.Confs.Database import getDatabase
from Api.Exceptions.Throws.NotFoundException import NotFoundException
from Api.Modules.Products.v1.Models.Product import Product


class ProductsDatabaseRepository:
    def __init__(self, database: Session = Depends(getDatabase)) -> None:
        self.database = database

    def create(self, product: Product) -> None:
        try:
            self.database.add(product)
        finally:
            self.database.flush()

    def getAll(self) -> list[Product]:
        return self.database.query(Product).all()

    def get(self, product_id: UUID) -> Product:
        return self.database.query(Product).get(product_id)

    def update(self, product: Product) -> float:
        try:
            if(self.database.query(Product).filter(Product.id == product.id).update(product.toDict()) == 0):
                raise NotFoundException
        
            return True
        finally:
            self.database.flush()

    def delete(self, product_id: UUID) -> float:
        if (self.database.query(Product).filter(Product.id == product_id).delete() == 0):
            raise NotFoundException

        return True
