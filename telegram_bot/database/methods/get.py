from sqlalchemy import exc, select

from telegram_bot.database.main import Database
from telegram_bot.database.models import User


def get_user_by_id_telegram_id(telegram_id: int) -> User | None:
    try:
        return Database().session.query(User).filter(User.telegram_id == telegram_id).one()
    except exc.NoResultFound:
        return None


def get_users_with_sessions() -> list:
    return Database().session.query(User).filter(User.session).all()


def get_all_telegram_id() -> list[tuple[int]]:
    return Database().session.query(User.telegram_id).all()
