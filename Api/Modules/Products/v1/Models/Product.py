from sqlalchemy import Column, Uuid, String, Float, Integer, text
from Api.Confs.Database import Base


class Product(Base):
  __tablename__ = "Products"

  id = Column(Uuid(as_uuid = True), primary_key = True, server_default = text("uuid_generate_v4()"))
  name = Column(String, nullable = False, unique = True)
  description = Column(String, nullable = True)
  price = Column(Float(asdecimal = True, precision = 10, decimal_return_scale = 2), nullable = True, default = 0.00)
  stock = Column(Integer, nullable = True, default = 0)

  def toDict(self):
    return {
      c.name: getattr(self, c.name)
        for c in self.__table__.columns if getattr(self, c.name) is not None
    }
