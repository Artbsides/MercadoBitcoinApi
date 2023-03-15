from uuid import UUID
from typing import Optional
from pydantic import BaseModel
from Api.Modules.Products.v1.Models.Product import Product


class ProductDto(BaseModel):
  name: str

  def toModel(self, product_id: Optional[UUID] = None) -> Product:
    product: Product = Product(
      name = self.name
    )

    if product_id:
      product.id = product_id

    return product
