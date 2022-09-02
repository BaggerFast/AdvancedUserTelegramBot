from sqlalchemy import exc, select

from telegram_bot.database.main import Database
from telegram_bot.database.models import User


def get_user_by_id_telegram_id(telegram_id: int) -> User | None:
    try:
        return Database().session.query(User).filter(User.telegram_id == telegram_id).one()
    except exc.NoResultFound:
        return None


def get_users_with_sessions() -> list[tuple[User]] | None:
    select_query = select(User).where(User.session)
    return Database().session.execute(select_query).fetchall()


def get_all_users():
    session = Database().session
    select_query = select(User.telegram_id)
    return session.execute(select_query).fetchall()
