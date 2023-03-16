import os
import jwt
import unittest
import pytest

from Main import app
from http import HTTPStatus
from uuid import UUID, uuid4
from datetime import datetime, timedelta
from fastapi import Response
from fastapi.testclient import TestClient
from Api.Modules.Products.v1.Models.Product import Product
from Api.Modules.Products.v1.Repositories.Cache import ProductsCacheRepository
from Api.Modules.Products.v1.Repositories.Database import ProductsDatabaseRepository
from Api.Exceptions.Throws.UnauthorizedTokenError import UnauthorizedTokenError


class TestProductsController(unittest.TestCase):
  class ProductsRepositoryMock:
    def create(self, _: Product):
      pass

    def getAll(self):
      pass

    def get(self, _: UUID):
      pass

    def update(self, _: Product):
      return 1

    def delete(self, _: UUID):
      return 1

  app.dependency_overrides[ProductsCacheRepository] = ProductsRepositoryMock
  app.dependency_overrides[ProductsDatabaseRepository] = ProductsRepositoryMock

  jwtToken = jwt.encode({ "exp": datetime.now() + timedelta(seconds=30) },
    os.getenv("JWT_SECRET"), os.getenv("JWT_ALGORITHM"))

  client = TestClient(app)

  def testPost(self) -> None:
    with pytest.raises(UnauthorizedTokenError):
      self.client.post("/v1/products")

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
    with pytest.raises(UnauthorizedTokenError):
      self.client.get("/v1/products")

    response: Response = self.client.get("/v1/products",
      headers = {
        "Authorization": f"Bearer { self.jwtToken }"
      }
    )

    self.assertIs(response.status_code, int(HTTPStatus.OK))
    self.assertIsNotNone(response.content)

  def testGet(self) -> None:
    with pytest.raises(UnauthorizedTokenError):
      self.client.get(f"/v1/products/{ uuid4() }")

    response: Response = self.client.get(f"/v1/products/{ uuid4() }",
      headers = {
        "Authorization": f"Bearer { self.jwtToken }"
      }
    )

    self.assertIs(response.status_code, int(HTTPStatus.OK))
    self.assertIsNotNone(response.content)

  def testUpdate(self) -> None:
    with pytest.raises(UnauthorizedTokenError):
      self.client.patch(f"/v1/products/{ uuid4() }")

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
    with pytest.raises(UnauthorizedTokenError):
      self.client.delete(f"/v1/products/{ uuid4() }")

    response: Response = self.client.delete(f"/v1/products/{ uuid4() }",
      headers = {
        "Authorization": f"Bearer { self.jwtToken }"
      }
    )

    self.assertIs(response.status_code, int(HTTPStatus.NO_CONTENT))
    self.assertIs(response.content, b"")
