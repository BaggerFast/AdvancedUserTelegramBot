from telegram_bot.database.models import User
from telegram_bot.database.main import Database


def is_admin(telegram_id: int) -> bool:
    return bool(Database().session.query(User.admin).filter(User.telegram_id == telegram_id).one()[0])
