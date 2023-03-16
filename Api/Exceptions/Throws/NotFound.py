from http import HTTPStatus
from typing import Optional


class NotFound(Exception):
  def __init__(self, exception: Optional[Exception] = None) -> None:
    self.attrs: dict = {
      "title": "Not Found",
      "error_messages": [
        "Resource not found"
      ]
    }

    self.status_code = HTTPStatus.NOT_FOUND
