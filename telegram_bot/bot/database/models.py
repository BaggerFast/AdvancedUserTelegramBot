from sqlalchemy import Column, Integer

from .main_database import *


class User(Database.Base):
    __tablename__ = "USER"
    id = Column(Integer(), primary_key=True)
    telegram_id = Column(Integer(), nullable=False)
    vip = Column(Integer(), default=0)


def register_models():
    Database.Base.metadata.create_all(Database().engine)
