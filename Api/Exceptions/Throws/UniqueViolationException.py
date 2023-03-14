from http import HTTPStatus


class UniqueViolationException(Exception):
    title: str = "UniqueViolation"
    message: str = "Unique key database violation"
    status_code = HTTPStatus.BAD_REQUEST
