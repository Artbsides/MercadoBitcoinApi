import importlib

from fastapi import Request
from fastapi.responses import JSONResponse
from http import HTTPStatus
from Api.Exceptions.Throws.InternalServerError import InternalServerError


class ExceptionHandler:
  def throw(_: Request, exception: Exception) -> JSONResponse:
    klass = type(exception).__name__

    try:
      exception: Exception = \
        getattr(importlib.import_module(f"Api.Exceptions.Throws.{ klass }"), klass)(exception)
    except Exception as e:
      exception: Exception = InternalServerError(e)

    if exception.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
      print("==== send exception to sentry")

    return JSONResponse({ "data": exception.attrs }, exception.status_code)
