from sqlalchemy import select

from telegram_bot.database.main import Database
from telegram_bot.database.models import User, Session


def create_user(telegram_id: int) -> None:
    select_query = select(User.telegram_id).where(User.telegram_id == telegram_id)
    session = Database().session
    if session.execute(select_query).fetchone():
        return
    insert_query = User(telegram_id=telegram_id)
    session.add(insert_query)
    session.commit()


def create_user_bot_session(user: User, user_bot_session: str) -> None:
    session = Database().session
    session.add(Session(user_id=user.id, session=user_bot_session))
    session.commit()
