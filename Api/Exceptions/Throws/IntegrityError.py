from http import HTTPStatus


class IntegrityError(Exception):
  def __init__(self, exception: Exception = None) -> None:
    self._error_messages: list[str] = [
      exception.orig.diag.message_primary,
      exception.orig.diag.message_detail
    ]

    getattr(self, type(exception.orig).__name__)()

  def UniqueViolation(self) -> None:
    self.attrs: dict = {
      "title": "Unique Key Violation",
      "error_messages": self._error_messages
    }

    self.status_code = HTTPStatus.BAD_REQUEST
