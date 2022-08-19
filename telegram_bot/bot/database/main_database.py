from typing import Final

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from misc import SingletonMeta


class Database(metaclass=SingletonMeta):
    Base: Final = declarative_base()

    def __init__(self):
        self.__engine = create_engine('sqlite:///database.db')
        self.__session = sessionmaker(bind=self.__engine)()

    @property
    def session(self):
        return self.__session

    @property
    def engine(self):
        return self.__engine
