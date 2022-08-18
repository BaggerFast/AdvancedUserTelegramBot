from sqlalchemy import Column, Integer

from .main_database import *


class User(BASE):
    __tablename__ = "users"
    id = Column(Integer(), primary_key=True)
    telegram_id = Column(Integer(), nullable=False)
    vip = Column(Integer(), default=0)


def register_models():
    BASE.metadata.create_all(engine)
