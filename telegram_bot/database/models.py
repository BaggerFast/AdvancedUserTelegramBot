from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .main import Database


class User(Database.BASE):
    __tablename__ = 'USER'
    id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer, nullable=False)
    admin = Column(Integer, default=0)
    session = relationship('Session', uselist=False, backref="USER", passive_deletes=True)


class Session(Database.BASE):
    __tablename__ = 'SESSION'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('USER.id', ondelete='CASCADE'), unique=True)
    string = Column(String, nullable=False)
    enable = Column(Integer, default=0)


def register_models():
    Database.BASE.metadata.create_all(Database().engine)
