from telegram_bot.database.main import Database
from telegram_bot.database.methods.get import get_user_by_telegram_id


def delete_session(telegram_id: int):
    session = Database().session
    user = get_user_by_telegram_id(telegram_id)
    if user and user.session:
        session.delete(user.session)
        session.commit()
