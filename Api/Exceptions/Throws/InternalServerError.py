from http import HTTPStatus
from typing import Optional


class InternalServerError(Exception):
  def __init__(self, exception: Optional[Exception] = None) -> None:
    self.attrs: dict = {
      "title": "Internal Server Error",
      "error_messages": [
        "An internal error occurred"
      ]
    }

    self.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
