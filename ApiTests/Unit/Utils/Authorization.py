import pytest
import unittest

from unittest import mock
from fastapi import Request
from Api.Exceptions.Throws.UnauthoeizedTokenError import UnauthoeizedTokenError

from Api.Utils.Authorization import authorization


class TestAuthorization(unittest.TestCase):
  @mock.patch("Api.Utils.Authorization.Request")
  def testToken(self, request: Request) -> None:
    request.scope = {
      "session": None
    }

    with pytest.raises(UnauthoeizedTokenError) as exception:
      authorization(request)

    self.assertIn(exception.typename, "UnauthoeizedTokenError")
