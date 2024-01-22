from telegram_bot.database.methods.delete import delete_session


def revoke_session(telegram_id: int):
    delete_session(telegram_id)
