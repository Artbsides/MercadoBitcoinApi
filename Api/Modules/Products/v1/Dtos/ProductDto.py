from uuid import UUID
from typing import Optional
from pydantic import BaseModel, NoneIsNotAllowedError, AnyStrMinLengthError, validator
from Api.Modules.Products.v1.Models.Product import Product


class ProductDto:
  class Create(BaseModel):
    name: str
    description: Optional[str]
    price: Optional[float]
    stock: Optional[int]

    @validator("name", pre=True, always=True)
    def notEmptyName(cls, value):
      if not value or not isinstance(value, str) or not value.strip():
        raise NoneIsNotAllowedError

      return value.strip()

    @validator("description", pre=True, always=True)
    def notEmptyDescription(cls, value):
      if not len(str(value).strip()):
        raise AnyStrMinLengthError(limit_value = 1)

      return value.strip() if value else value

    def toModel(self, product_id: Optional[UUID] = None) -> Product:
      product: Product = Product()

      for key, value in self.dict().items():
        setattr(product, key, value)

      if product_id:
        product.id = product_id

      return product

  class Update(Create):
    name: Optional[str]

    @validator("name", pre=True, always=True)
    def notEmptyName(cls, value):
      if not len(str(value).strip()):
        raise NoneIsNotAllowedError

      return value.strip() if value else value
