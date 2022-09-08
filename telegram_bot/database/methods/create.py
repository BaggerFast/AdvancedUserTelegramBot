import sqlalchemy.exc

from telegram_bot.database.main import Database
from telegram_bot.database.models import User, Session, Payment


def create_user(telegram_id: int) -> None:
    session = Database().session
    try:
        session.query(User.telegram_id).filter(User.telegram_id == telegram_id).one()
    except sqlalchemy.exc.NoResultFound:
        session.add(User(telegram_id=telegram_id))
        session.commit()


def create_session(user: User, user_bot_session: str) -> None:
    session = Database().session
    session.add(Session(user_id=user.id, string=user_bot_session))
    session.commit()


def create_user_payment(user: User, key) -> None:
    session = Database().session
    session.add(Payment(user_id=user.id, key=key))
    session.commit()
