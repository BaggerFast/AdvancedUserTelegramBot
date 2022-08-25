from loguru import logger
from sqlalchemy import select, update, exc

from .main_database import Database
from .models import User, Session


def create_user(telegram_id: int) -> None:
    select_query = select(User.telegram_id).where(User.telegram_id == telegram_id)
    session = Database().session
    if session.execute(select_query).fetchone():
        logger.debug(f"Такой пользователь уже есть в базе! Его Telegram-id - {telegram_id}")
        return
    insert_query = User(telegram_id=telegram_id)
    session.add(insert_query)
    session.commit()
    logger.debug(f"Добавлен новый юзер! Telegram-id - {telegram_id}")


def create_user_bot_session(user: User, user_bot_session: str):
    logger.debug("Зашёл в создание сессии")
    session = Database().session
    session.add(Session(user_id=user.id, session=user_bot_session))
    session.commit()
    logger.debug("После создания сессии в бд")


def get_user_by_id_telegram_id(telegram_id: int) -> User | None:
    try:
        return Database().session.query(User).filter(User.telegram_id == telegram_id).one()
    except exc.NoResultFound:
        return None


# region Vip

def check_vip(telegram_id) -> bool:
    select_query = select(User.vip).where(User.telegram_id == telegram_id)
    logger.debug("Отправляю запрос на проверку vip")
    result = bool(Database().session.execute(select_query).fetchone()[0])
    logger.debug(f"result: {result}")
    return result


def set_vip(telegram_id) -> None:
    update_query = update(User, values={User.vip: 1}).where(User.telegram_id == telegram_id)
    logger.debug("Отправляю запрос на установку vip статуса")
    session = Database().session
    session.execute(update_query)
    session.commit()
    logger.debug("Vip статус установлен!")


def get_users_with_sessions():
    select_query = select(User.telegram_id).where(User.session)
    result = Database().session.execute(select_query).fetchall()
    if not result:
        return None
    else:
        return result
# endregion
