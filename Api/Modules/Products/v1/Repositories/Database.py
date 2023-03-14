from uuid import UUID
from fastapi import Depends
from sqlalchemy.orm import Session
from Api.Confs.Database import getDatabase
from Api.Modules.Products.v1.Models.Product import Product
from Api.Exceptions.Throws.NotFound import NotFound


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
    product: Product = self.database.query(Product) \
      .get(product_id)

    if (product is None):
      raise NotFound

    return product

  def update(self, product: Product) -> float:
    try:
      status: int = self.database \
        .query(Product).filter(Product.id == product.id).update(product.toDict())

      if (status == 0):
        raise NotFound
    finally:
      self.database.flush()

    return status

  def delete(self, product_id: UUID) -> float:
    status: int = self.database \
      .query(Product).filter(Product.id == product_id).delete()

    if (status == 0):
      raise NotFound

    return status
