import unittest

from uuid import uuid4
from Api.Modules.Products.v1.Models.Product import Product


class TestProduct(unittest.TestCase):
  def testModel(self) -> None:
    data: Product = \
      Product()

    self.assertIsNone(data.id)
    self.assertIsNone(data.name)

    data.id = uuid4()
    data.name = "name"

    self.assertIsNotNone(data.id)
    self.assertIsNotNone(data.name)

  def testModelToDict(self) -> None:
    data: Product = \
      Product(name = "name").toDict()

    self.assertNotIn("id", data)
    self.assertIsNotNone(data["name"])

    data["id"] = uuid4()

    self.assertIsNotNone(data["id"])
    self.assertIsNotNone(data["name"])
