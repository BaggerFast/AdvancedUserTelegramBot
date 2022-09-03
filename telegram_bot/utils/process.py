from subprocess import Popen
from sys import executable

from misc.path import PathManager
from telegram_bot.database.methods.get import get_user_by_id_telegram_id

__process: dict[int, Popen] = {}


def start_process_if_sessions_exists(telegram_id: int):
    user = get_user_by_id_telegram_id(telegram_id)
    user_bot_app = PathManager.get("user_bot/main.py")
    if user and user.session:
        __process[telegram_id] = Popen([executable, user_bot_app, user.session.session,
                                        f'{telegram_id}', f'{user.vip}'])


def kill_process(telegram_id: int):
    if telegram_id in __process:
        __process[telegram_id].kill()
        del __process[telegram_id]


def check_process(telegram_id: int):
    return telegram_id in __process
