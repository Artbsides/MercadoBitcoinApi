import unittest

from http import HTTPStatus
from uuid import UUID, uuid4
from fastapi import Response
from fastapi.testclient import TestClient
from Api.Main import app
from Api.Modules.Products.v1.Models.Product import Product
from Api.Modules.Products.v1.Repositories.Cache import ProductsCacheRepository
from Api.Modules.Products.v1.Repositories.Database import ProductsDatabaseRepository


class TestProductsController(unittest.TestCase):
  client = TestClient(app)

  class ProductsRepositoryMock:
    def create(self, _: Product) -> Product:
      return None

    def getAll(self) -> list[Product]:
      return []

    def get(self, _: UUID) -> Product:
      return None

    def update(self, _: Product) -> None:
      pass

    def delete(self, _: UUID) -> None:
      pass

    def update(self, _: Product) -> int:
      return 1

    def delete(self, _: UUID) -> int:
      return 1

  def testPost(self) -> None:
    app.dependency_overrides[ProductsCacheRepository] = \
      self.ProductsRepositoryMock

    app.dependency_overrides[ProductsDatabaseRepository] = \
      self.ProductsRepositoryMock

    response: Response = self.client.post("/products", json = {
      "name": "name"
    })

    self.assertIs(response.status_code, int(HTTPStatus.CREATED))
    self.assertIsNotNone(response.content)

  def testGetAll(self) -> None:
    app.dependency_overrides[ProductsCacheRepository] = \
      self.ProductsRepositoryMock

    app.dependency_overrides[ProductsDatabaseRepository] = \
      self.ProductsRepositoryMock

    response: Response = self.client.get("/products")

    self.assertIs(response.status_code, int(HTTPStatus.OK))
    self.assertIsNotNone(response.content)

  def testGet(self) -> None:
    app.dependency_overrides[ProductsCacheRepository] = \
      self.ProductsRepositoryMock

    app.dependency_overrides[ProductsDatabaseRepository] = \
      self.ProductsRepositoryMock

    response: Response = self.client.get(f"/products/{ uuid4() }")

    self.assertIs(response.status_code, int(HTTPStatus.OK))
    self.assertIsNotNone(response.content)

  def testUpdate(self) -> None:
    app.dependency_overrides[ProductsCacheRepository] = \
      self.ProductsRepositoryMock

    app.dependency_overrides[ProductsDatabaseRepository] = \
      self.ProductsRepositoryMock

    response: Response = self.client.patch(f"/products/{ uuid4() }", json = {
      "name": "name"
    })

    self.assertIs(response.status_code, int(HTTPStatus.NO_CONTENT))
    self.assertIs(response.content, b"")

  def testDelete(self) -> None:
    app.dependency_overrides[ProductsCacheRepository] = \
      self.ProductsRepositoryMock

    app.dependency_overrides[ProductsDatabaseRepository] = \
      self.ProductsRepositoryMock

    response: Response = self.client.delete(f"/products/{ uuid4() }")

    self.assertIs(response.status_code, int(HTTPStatus.NO_CONTENT))
    self.assertIs(response.content, b"")
