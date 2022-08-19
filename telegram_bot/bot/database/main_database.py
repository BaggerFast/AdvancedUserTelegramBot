from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

path = '/path/'
engine = create_engine('sqlite:///telegram_bot/bot/database/FileDatabase/Database.db')
BASE = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()



