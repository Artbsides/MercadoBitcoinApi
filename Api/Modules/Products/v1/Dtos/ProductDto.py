from uuid import UUID
from typing import Optional
from pydantic import BaseModel, NoneIsNotAllowedError, validator
from Api.Modules.Products.v1.Models.Product import Product


class ProductDto(BaseModel):
  name: str

  @validator("name", pre=True, always=True)
  def notEmptyName(cls, value):
    if not value or not isinstance(value, str) or not value.strip():
      raise NoneIsNotAllowedError

    return value.strip()

  def toModel(self, product_id: Optional[UUID] = None) -> Product:
    product: Product = Product(
      name = self.name
    )

    if product_id:
      product.id = product_id

    return product
