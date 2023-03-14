from http import HTTPStatus


class NotFoundException(Exception):
    title: str = "NotFound"
    message: str = "Resource not found"
    status_code = HTTPStatus.NOT_FOUND
