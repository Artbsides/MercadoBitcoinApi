import unittest

from http import HTTPStatus
from Api.Exceptions.Throws.UnauthoeizedTokenError import UnauthoeizedTokenError


class TestUnauthoeizedTokenError(unittest.TestCase):
  def testException(self) -> None:
    exception: UnauthoeizedTokenError = UnauthoeizedTokenError()

    self.assertIsNotNone(exception.attrs)
    self.assertIs(exception.status_code, HTTPStatus.UNAUTHORIZED)
