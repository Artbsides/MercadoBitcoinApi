import uuid

from sqlalchemy import Column, Uuid, String
from Api.Confs.Database import Base


class Product(Base):
    __tablename__ = "Products"

    id = Column(Uuid(as_uuid=True), primary_key=True, default=str(uuid.uuid4()))
    name = Column(String, nullable=False, unique=True)

    def to_dict(self):
        return { c.name: getattr(self, c.name)
            for c in self.__table__.columns
        }
