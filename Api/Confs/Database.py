import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker


Engine = create_engine(
  os.getenv("POSTGRES_CONNECTION_STRING"), echo=True)

Base = declarative_base()
SessionLocal = sessionmaker(bind = Engine)

def getDatabase():
  database = scoped_session(SessionLocal)

  try:
    yield database
  finally:
    database.close()
