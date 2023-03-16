import pytest
import unittest

from uuid import uuid4
from pydantic import ValidationError
from Api.Modules.Products.v1.Dtos.ProductDto import ProductDto
from Api.Modules.Products.v1.Models.Product import Product


class TestProductDto(unittest.TestCase):
  def testDto(self) -> None:
    with pytest.raises(ValidationError) as exception:
      ProductDto()

    self.assertIn("field required (type=value_error.missing)", str(exception.value))

    dto: ProductDto = \
      ProductDto(name="name")

    self.assertIsNotNone(dto.name)

  def testDtoToModel(self) -> None:
    model: Product = \
      ProductDto(name="name").toModel(uuid4())

    self.assertIsNotNone(model.id)
    self.assertIsNotNone(model.name)
