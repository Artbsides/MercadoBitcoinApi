import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker, Session


Engine = create_engine(
  f'postgresql+psycopg2://{ os.getenv("POSTGRES_CONNECTION_STRING") }', echo = True)

Base = declarative_base()
SessionLocal = sessionmaker(bind = Engine)

def getDatabase() -> Session:
  session = scoped_session(SessionLocal)

  try:
    yield session

    if session.new or session.dirty or session.delete:
      session.commit()
  finally:
    session.close()
