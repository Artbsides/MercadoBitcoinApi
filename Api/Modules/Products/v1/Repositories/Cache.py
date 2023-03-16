import json

from uuid import UUID
from fastapi import Depends
from redis import Redis
from fastapi.encoders import jsonable_encoder
from Api.Confs.Cache import getCache
from Api.Modules.Products.v1.Models.Product import Product


class ProductsCacheRepository:
  def __init__(self, cache: Redis = Depends(getCache)) -> None:
    self.cache = cache

  def create(self, product: Product) -> None:
    self.cache.set(str(product.id),
      json.dumps(jsonable_encoder(product.toDict())))

  def getAll(self) -> list[Product]:
    return [
      json.loads(product) for product in self.cache.mget(self.cache.keys())
    ]

  def get(self, product_id: UUID) -> str:
    return json.loads(self.cache.get(str(product_id)) or "{}")

  def update(self, product: Product) -> None:
    self.create(product)

  def delete(self, product_id: UUID) -> None:
    self.cache.delete(str(product_id))
