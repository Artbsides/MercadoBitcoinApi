import os
from redis import Redis


def getCache() -> Redis:
  session = Redis.from_url(
    os.getenv("REDIS_CONNECTION_STRING"), encoding = "utf-8", socket_timeout = 15, decode_responses = True
  )

  try:
    yield session
  finally:
    session.close()
