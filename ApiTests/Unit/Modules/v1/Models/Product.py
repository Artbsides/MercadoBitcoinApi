import unittest

from uuid import uuid4
from Api.Modules.Products.v1.Models.Product import Product


class TestProduct(unittest.TestCase):
  def testModel(self) -> None:
    model: Product = \
      Product()

    self.assertIsNone(model.id)
    self.assertIsNone(model.name)

    model.id = uuid4()
    model.name = "name"

    self.assertIsNotNone(model.id)
    self.assertIsNotNone(model.name)

  def testModelToDict(self) -> None:
    dict: Product = \
      Product(name="name").toDict()

    self.assertIsNone(dict["id"])
    self.assertIsNotNone(dict["name"])

    dict["id"] = uuid4()

    self.assertIsNotNone(dict["id"])
    self.assertIsNotNone(dict["name"])
