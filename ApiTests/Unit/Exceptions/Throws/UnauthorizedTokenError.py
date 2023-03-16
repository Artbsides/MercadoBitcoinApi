import unittest

from http import HTTPStatus
from Api.Exceptions.Throws.UnauthorizedTokenError import UnauthorizedTokenError


class TestUnauthorizedTokenError(unittest.TestCase):
  def testException(self) -> None:
    exception: UnauthorizedTokenError = UnauthorizedTokenError()

    self.assertIsNotNone(exception.attrs)
    self.assertIs(exception.status_code, HTTPStatus.UNAUTHORIZED)
