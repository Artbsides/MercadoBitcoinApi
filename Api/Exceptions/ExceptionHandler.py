from http import HTTPStatus
import importlib

from fastapi import Request
from fastapi.responses import JSONResponse
from Api.Exceptions.Throws.InternalServerErrorException import InternalServerErrorException


class ExceptionHandler:
  def throw(request: Request, exception: Exception) -> JSONResponse:
    klass = type(exception).__name__

    try:
      exception: Exception = \
        getattr(importlib.import_module(f"Api.Exceptions.Throws.{ klass }"), klass)(exception)
    except Exception as e:
      exception: Exception = InternalServerErrorException(e)

    if (exception.status_code == HTTPStatus.INTERNAL_SERVER_ERROR):
      print("==== send exception to sentry")

    return JSONResponse({ "data": exception.attrs }, exception.status_code)
