from sqlalchemy import Column, Uuid, String, text
from Api.Confs.Database import Base


class Product(Base):
  __tablename__ = "Products"

  id = Column(Uuid(as_uuid=True), primary_key=True, server_default=text("uuid_generate_v4()"))
  name = Column(String, nullable=False, unique=True)

  def toDict(self):
    return { c.name: getattr(self, c.name)
      for c in self.__table__.columns
    }
