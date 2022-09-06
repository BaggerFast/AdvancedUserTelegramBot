from subprocess import Popen
from sys import executable

from misc.path import PathManager
from telegram_bot.database.methods.get import get_user_by_telegram_id
from telegram_bot.database.methods.update import update_session_status

__process: dict[int, Popen] = {}


def start_process_if_sessions_exists(telegram_id: int) -> None:
    user = get_user_by_telegram_id(telegram_id)
    user_bot_app = PathManager.get("run_user_bot.py")
    if not (user and user.session):
        return
    update_session_status(telegram_id, 1)
    __process[telegram_id] = Popen([executable, user_bot_app, user.session.string, f'{telegram_id}', f'{user.vip}'])


def kill_process(telegram_id: int) -> None:
    if telegram_id in __process:
        update_session_status(telegram_id, 0)
        __process[telegram_id].kill()
        del __process[telegram_id]


def check_process(telegram_id: int) -> bool:
    return telegram_id in __process
