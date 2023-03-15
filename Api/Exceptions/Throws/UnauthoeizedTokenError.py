from http import HTTPStatus
from typing import Optional


class UnauthoeizedTokenError(Exception):
  def __init__(self, exception: Optional[Exception] = None) -> None:
    self.attrs: dict = {
      "title": "Unauthoeized",
      "error_messages": [
        "Check your bearer token, you might not be authorized"
      ]
    }

    self.status_code = HTTPStatus.UNAUTHORIZED
