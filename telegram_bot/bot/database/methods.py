import loguru
from sqlalchemy import select, update

from .main_database import session
from .models import User


def add_user(telegram_id) -> None:
    select_query = select(User.telegram_id).where(User.telegram_id == telegram_id)
    loguru.logger.debug("Проверка на регистрацию")
    result = session.execute(select_query).fetchone()
    if result:
        loguru.logger.debug(f"Такой пользователь уже есть в базе! Его Telegram-id - {telegram_id}")
        return
    insert_query = User(telegram_id=telegram_id)
    session.add(insert_query)
    session.commit()
    loguru.logger.debug(f"Добавлен новый юзер! Telegram-id - {telegram_id}")


def check_vip(telegram_id) -> bool:
    select_query = select(User.vip).where(User.telegram_id == telegram_id)
    loguru.logger.debug("Отпровляю запрос на проверку vip")
    result = session.execute(select_query).fetchone()[0]
    loguru.logger.debug(f"result: {bool(result)}")
    if result == 0:
        return False
    elif result == 1:
        return True


def set_vip(telegram_id) -> None:
    update_query = update(User, values={User.vip: 1}).where(User.telegram_id == telegram_id)
    loguru.logger.debug("Отправляю запрос на установку vip статуса")
    session.execute(update_query)
    session.commit()
    loguru.logger.debug("Vip статус установлен!")
