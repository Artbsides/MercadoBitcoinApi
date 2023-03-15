import unittest

from http import HTTPStatus
from Api.Exceptions.Throws.InternalServerError import InternalServerError


class TestInternaServerError(unittest.TestCase):
  def testException(self) -> None:
    exception: InternalServerError = InternalServerError()

    self.assertIsNotNone(exception.attrs)
    self.assertIs(exception.status_code, HTTPStatus.INTERNAL_SERVER_ERROR)
