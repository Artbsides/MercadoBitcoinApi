import pytest
import unittest

from uuid import uuid4
from pydantic import ValidationError
from Api.Modules.Products.v1.Dtos.ProductDto import ProductDto
from Api.Modules.Products.v1.Models.Product import Product


class TestProductDto:
  class TestCreate(unittest.TestCase):
    def testDto(self) -> None:
      with pytest.raises(ValidationError) as exception:
        ProductDto.Create()

      self.assertIn("value_error.missing", str(exception.value))

      with pytest.raises(ValidationError) as exception:
        ProductDto.Create(name = "")

      self.assertIn("type_error.none.not_allowed", str(exception.value))

      with pytest.raises(ValidationError) as exception:
        ProductDto.Create(name = "name", description = "")

      self.assertIn("value_error.any_str.min_length", str(exception.value))

      data: ProductDto = \
        ProductDto.Create(name = "name")

      self.assertIsNotNone(data.name)

    def testDtoToModel(self) -> None:
      data: Product = \
        ProductDto.Create(name = "name").toModel(uuid4())

      self.assertIsNotNone(data.id)
      self.assertIsNotNone(data.name)

  class TestUpdate(unittest.TestCase):
    def testDto(self) -> None:
      with pytest.raises(ValidationError) as exception:
        ProductDto.Update(name = "")

      self.assertIn("type_error.none.not_allowed", str(exception.value))

      data: ProductDto = \
        ProductDto.Update(name = "name")

      self.assertIsNotNone(data.name)

    def testDtoToModel(self) -> None:
      data: Product = \
        ProductDto.Update(name = "name").toModel(uuid4())

      self.assertIsNotNone(data.id)
      self.assertIsNotNone(data.name)
