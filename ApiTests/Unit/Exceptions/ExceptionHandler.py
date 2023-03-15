import unittest

from unittest import mock
from http import HTTPStatus
from asyncpg import InternalServerError
from fastapi import Request
from fastapi.responses import JSONResponse
from Api.Exceptions.ExceptionHandler import ExceptionHandler
from Api.Exceptions.Throws.NotFound import NotFound


class TestExceptionHandler(unittest.TestCase):
  @mock.patch("Api.Exceptions.ExceptionHandler.Request")
  def testThrow(self, request: Request) -> None:
    request.scope = {
      "session": None
    }

    excpetion: JSONResponse = ExceptionHandler \
      .throw(request, NotFound())
    
    self.assertIs(excpetion.status_code, HTTPStatus.NOT_FOUND)
    self.assertIsNotNone(excpetion.body)

    self.assertIsInstance(excpetion, JSONResponse)

  @mock.patch("Api.Exceptions.ExceptionHandler.Request")
  def testThrownException(self, request: Request) -> None:
    request.scope = {
      "session": None
    }

    excpetion: JSONResponse = ExceptionHandler \
      .throw(request, AttributeError())
    
    self.assertIs(excpetion.status_code, HTTPStatus.INTERNAL_SERVER_ERROR)
    self.assertIsNotNone(excpetion.body)

    self.assertIsInstance(excpetion, JSONResponse)

  @mock.patch("Api.Exceptions.ExceptionHandler.Request")
  def testThrowInternalServerErrror(self, request: Request) -> None:
    request.scope = {
      "session": None
    }

    excpetion: JSONResponse = ExceptionHandler \
      .throw(request, InternalServerError())
    
    self.assertIs(excpetion.status_code, HTTPStatus.INTERNAL_SERVER_ERROR)
    self.assertIsNotNone(excpetion.body)

    self.assertIsInstance(excpetion, JSONResponse)
