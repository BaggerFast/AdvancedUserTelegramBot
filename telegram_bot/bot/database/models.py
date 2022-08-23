# https://stackoverflow.com/questions/25002620/argumenterror-relationship-expects-a-class-or-mapper-argument

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .main_database import *


class User(Database.Base):
    __tablename__ = 'USER'
    id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer, nullable=False)
    vip = Column(Integer, default=0)
    session = relationship('Session', uselist=False, backref="USER")


class Session(Database.Base):
    __tablename__ = 'SESSION'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('USER.id'), unique=True)
    session = Column(String, nullable=False)


def register_models():
    Database.Base.metadata.create_all(Database().engine)
