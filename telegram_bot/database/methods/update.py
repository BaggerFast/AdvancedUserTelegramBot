from sqlalchemy import update

from telegram_bot.database.main import Database
from telegram_bot.database.models import User


def set_vip(telegram_id: int) -> None:
    Database().session.query(User).filter(User.telegram_id == telegram_id).update(values={User.vip: 1})
    Database().session.commit()


def set_admin(telegram_id: int) -> None:
    Database().session.query(User).filter(User.telegram_id == telegram_id).update(values={User.admin: 1})
    Database().session.commit()
