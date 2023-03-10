import os
from redis import Redis


def getCache():
    session = Redis.from_url(os.getenv("REDIS_CONNECTION_STRING"),
        encoding="utf-8", decode_responses=True)

    try:
        yield session
    finally:
        session.close()
