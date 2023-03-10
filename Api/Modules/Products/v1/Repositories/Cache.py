import json
import pickle
from uuid import UUID
from fastapi import Depends
from redis import Redis
from fastapi.encoders import jsonable_encoder
from Api.Confs.Cache import getCache
from Api.Modules.Products.v1.Models.Product import Product


class ProductsCacheRepository:
    def __init__(self, cache = Depends(getCache)) -> None:
        self.cache = cache

    def create(self, product: Product) -> Product:
        self.cache.set(str(product.id), json.dumps(jsonable_encoder(product.to_dict())))

        return product

    def get(self, product_id: UUID) -> Product:
        return json.loads(self.cache.get(str(product_id))
            or "{}")

    def delete(self, product_id: UUID) -> Product:
        return self.cache.delete(product_id)
