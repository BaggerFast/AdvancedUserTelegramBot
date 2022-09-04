from telegram_bot.database.main import Database
from telegram_bot.database.methods.get import get_user_by_telegram_id
from telegram_bot.database.models import User


def set_vip(telegram_id: int) -> None:
    Database().session.query(User).filter(User.telegram_id == telegram_id).update(values={User.vip: 1})
    Database().session.commit()


def set_admin(telegram_id: int) -> None:
    Database().session.query(User).filter(User.telegram_id == telegram_id).update(values={User.admin: 1})
    Database().session.commit()


def update_session_status(telegram_id, enable) -> None:
    user = get_user_by_telegram_id(telegram_id)
    if user and user.session:
        user.session.enable = int(enable)
    Database().session.commit()
