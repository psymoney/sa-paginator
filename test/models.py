from sqlalchemy import *
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True)
    name = Column(TEXT)
    value = Column(Integer)
    value_2 = Column(Integer)
