import os
import jwt

from fastapi import Request
from Api.Exceptions.Throws.UnauthoeizedTokenError import UnauthoeizedTokenError


def authorization(request: Request) -> None:
  try:
    jwt.decode(request.headers["Authorization"].replace("Bearer ", ""), os.getenv("JWT_SECRET"), [
      os.getenv("JWT_ALGORITHM")
    ])
  except:
    raise UnauthoeizedTokenError
