import unittest

from http import HTTPStatus
from Api.Exceptions.Throws.NotFound import NotFound


class TestNotFound(unittest.TestCase):
  def testException(self) -> None:
    exception: NotFound = NotFound()

    self.assertIsNotNone(exception.attrs)
    self.assertIs(exception.status_code, HTTPStatus.NOT_FOUND)
