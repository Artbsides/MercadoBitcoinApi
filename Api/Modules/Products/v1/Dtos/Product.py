from pydantic import BaseModel, Field

from Api.Modules.Products.v1.Models.Product import Product


class ProductDto(BaseModel):
    name: str

    def toModel(self):
        return Product(
            name = self.name
        )
