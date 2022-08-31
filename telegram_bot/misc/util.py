from sys import executable
from subprocess import Popen
from misc.path import PathManager
from telegram_bot.database.methods import check_vip
from telegram_bot.keyboards import KB_STOP_PRO_BOT, KB_START_PRO, KB_START_TRIAL, \
    KB_STOP_TRIAL_BOT


def start_user_bot(string_session: str, telegram_id: int, vip_status: int = 0):
    return Popen([executable, PathManager.get("user_bot/main.py"), string_session, f'{telegram_id}', f'{vip_status}'])


def get_main_keyboard(user_id: int, in_process: bool):
    is_vip = check_vip(user_id)
    if in_process:
        return KB_STOP_PRO_BOT if is_vip else KB_STOP_TRIAL_BOT
    return KB_START_PRO if is_vip else KB_START_TRIAL
