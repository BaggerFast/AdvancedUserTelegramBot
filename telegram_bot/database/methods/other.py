from sqlalchemy import select

from telegram_bot.database.main import Database
from telegram_bot.database.methods.create import create_user
from telegram_bot.database.methods.get import get_user_by_id_telegram_id
from telegram_bot.database.models import User


def is_vip(telegram_id) -> bool:
    select_query = select(User.vip).where(User.telegram_id == telegram_id)
    result = bool(Database().session.execute(select_query).fetchone()[0])
    return result


def is_admin(telegram_id: int) -> bool:
    create_user(telegram_id)
    select_query = select(User.admin).where(User.telegram_id == telegram_id)
    session = Database().session
    result = session.execute(select_query).fetchone()
    return bool(result[0])


def switch_vip(telegram_id: int):
    user = get_user_by_id_telegram_id(telegram_id)
    if user:
        user.vip = not user.vip
        Database().session.commit()
