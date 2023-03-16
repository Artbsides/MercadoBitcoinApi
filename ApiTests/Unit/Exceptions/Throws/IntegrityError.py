import unittest

from http import HTTPStatus
from psycopg2._psycopg import Diagnostics
from Api.Exceptions.Throws.IntegrityError import IntegrityError


class TestIntegrityError(unittest.TestCase):
  def testUniqueViolation(self) -> None:
    class UniqueViolation:
      diag: Diagnostics = type("Diagnostics", (Diagnostics,), {
        "message_detail": "Detail",
        "message_primary": "Message"
      })

    class PGSQLIntegrityError:
      orig: UniqueViolation = UniqueViolation()

    exception: IntegrityError = IntegrityError(PGSQLIntegrityError())

    self.assertIsNotNone(exception.attrs)
    self.assertIs(exception.status_code, HTTPStatus.BAD_REQUEST)
