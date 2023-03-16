import os
import jwt

from typing import Optional
from fastapi import Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from Api.Exceptions.Throws.UnauthorizedTokenError import UnauthorizedTokenError


class Authorization(HTTPBearer):
  def __init__(self) -> None:
    super(Authorization, self).__init__()

  async def __call__(self, request: Request) -> Optional[HTTPAuthorizationCredentials]:
    try:
      auth: HTTPAuthorizationCredentials = \
        await super(Authorization, self).__call__(request)

      jwt.decode(auth.credentials, os.getenv("JWT_SECRET"), [ os.getenv("JWT_ALGORITHM") ])
    except Exception:
      raise UnauthorizedTokenError
