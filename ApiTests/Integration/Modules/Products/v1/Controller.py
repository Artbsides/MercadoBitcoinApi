import os
import jwt
import unittest
import datetime

from http import HTTPStatus
from uuid import UUID, uuid4
from fastapi import Response
from fastapi.testclient import TestClient
from Api.Main import app
from Api.Modules.Products.v1.Models.Product import Product
from Api.Modules.Products.v1.Repositories.Cache import ProductsCacheRepository
from Api.Modules.Products.v1.Repositories.Database import ProductsDatabaseRepository


class TestProductsController(unittest.TestCase):
  jwtToken = jwt.encode({
    "exp": datetime.datetime.now() + datetime.timedelta(seconds=30) }, os.getenv("JWT_SECRET"), os.getenv("JWT_ALGORITHM"))

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

    response: Response = self.client.post("/v1/products",
      json = {
        "name": "name"
      },
      headers = {
        "Authorization": f"Bearer { self.jwtToken }"
      }
    )

    self.assertIs(response.status_code, int(HTTPStatus.CREATED))
    self.assertIsNotNone(response.content)

  def testGetAll(self) -> None:
    app.dependency_overrides[ProductsCacheRepository] = \
      self.ProductsRepositoryMock

    app.dependency_overrides[ProductsDatabaseRepository] = \
      self.ProductsRepositoryMock

    response: Response = self.client.get("/v1/products",
      headers = {
        "Authorization": f"Bearer { self.jwtToken }"
      }
    )

    self.assertIs(response.status_code, int(HTTPStatus.OK))
    self.assertIsNotNone(response.content)

  def testGet(self) -> None:
    app.dependency_overrides[ProductsCacheRepository] = \
      self.ProductsRepositoryMock

    app.dependency_overrides[ProductsDatabaseRepository] = \
      self.ProductsRepositoryMock

    response: Response = self.client.get(f"/v1/products/{ uuid4() }",
      headers = {
        "Authorization": f"Bearer { self.jwtToken }"
      }
    )

    self.assertIs(response.status_code, int(HTTPStatus.OK))
    self.assertIsNotNone(response.content)

  def testUpdate(self) -> None:
    app.dependency_overrides[ProductsCacheRepository] = \
      self.ProductsRepositoryMock

    app.dependency_overrides[ProductsDatabaseRepository] = \
      self.ProductsRepositoryMock

    response: Response = self.client.patch(f"/v1/products/{ uuid4() }",
      json = {
        "name": "name"
      },
      headers = {
        "Authorization": f"Bearer { self.jwtToken }"
      }
    )

    self.assertIs(response.status_code, int(HTTPStatus.NO_CONTENT))
    self.assertIs(response.content, b"")

  def testDelete(self) -> None:
    app.dependency_overrides[ProductsCacheRepository] = \
      self.ProductsRepositoryMock

    app.dependency_overrides[ProductsDatabaseRepository] = \
      self.ProductsRepositoryMock

    response: Response = self.client.delete(f"/v1/products/{ uuid4() }",
      headers = {
        "Authorization": f"Bearer { self.jwtToken }"
      }
    )

    self.assertIs(response.status_code, int(HTTPStatus.NO_CONTENT))
    self.assertIs(response.content, b"")
