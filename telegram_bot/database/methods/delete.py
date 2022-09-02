from telegram_bot.database.main import Database
from telegram_bot.database.methods.get import get_user_by_id_telegram_id


def delete_session(telegram_id: int):
    user = get_user_by_id_telegram_id(telegram_id)
    if user and user.session:
        Database().session.delete(user.session)
        Database().session.commit()
