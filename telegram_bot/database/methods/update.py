from sqlalchemy import update

from telegram_bot.database.main import Database
from telegram_bot.database.models import User


def set_vip(telegram_id: int) -> None:
    update_query = update(User, values={User.vip: 1}).where(User.telegram_id == telegram_id)
    session = Database().session
    session.execute(update_query)
    session.commit()


def set_admin(telegram_id: int) -> None:
    session = Database().session
    update_query = update(User, values={User.admin: 1}).where(User.telegram_id == telegram_id)
    session.execute(update_query)
    session.commit()