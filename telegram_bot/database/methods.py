from loguru import logger
from sqlalchemy import select, update, exc

from .main_database import Database
from .models import User, Session


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


def get_user_by_id_telegram_id(telegram_id: int) -> User | None:
    try:
        return Database().session.query(User).filter(User.telegram_id == telegram_id).one()
    except exc.NoResultFound:
        return None


# region Vip

def check_vip(telegram_id: int) -> bool:
    select_query = select(User.vip).where(User.telegram_id == telegram_id)
    return bool(Database().session.execute(select_query).fetchone()[0])


def set_vip(telegram_id: int) -> None:
    update_query = update(User, values={User.vip: 1}).where(User.telegram_id == telegram_id)
    session = Database().session
    session.execute(update_query)
    session.commit()


def switch_vip(telegram_id: int):
    user = get_user_by_id_telegram_id(telegram_id)
    if user:
        user.vip = not user.vip
        Database().session.commit()


def get_users_with_sessions() -> list[tuple[User]] | None:
    select_query = select(User).where(User.session)
    return Database().session.execute(select_query).fetchall()


def check_admin(telegram_id: int) -> bool:
    create_user(telegram_id)
    select_query = select(User.admin).where(User.telegram_id == telegram_id)
    session = Database().session
    result = session.execute(select_query).fetchone()
    return bool(result[0])


def set_admin(telegram_id: int) -> None:
    session = Database().session
    update_query = update(User, values={User.admin: 1}).where(User.telegram_id == telegram_id)
    session.execute(update_query)
    session.commit()


def get_all_users():
    session = Database().session
    select_query = select(User.telegram_id)
    return session.execute(select_query).fetchall()


def delete_session(telegram_id: int):
    user = get_user_by_id_telegram_id(telegram_id)
    if user and user.session:
        Database().session.delete(user.session)
        Database().session.commit()

# endregion
