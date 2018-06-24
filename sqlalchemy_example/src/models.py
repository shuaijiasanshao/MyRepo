# coding: utf-8
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):

    __tablename__ = 'user'

    id = Column(String(36), primary_key=True, nullable=False)
    name = Column(String(20), nullable=False)
    sex = Column(String(6))
    age = Column(Integer)
    create_at = Column(DateTime)
