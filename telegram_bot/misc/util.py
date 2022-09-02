from copy import deepcopy
from sys import executable
from subprocess import Popen
from aiogram.types import KeyboardButton
from misc.path import PathManager
from telegram_bot.database.methods import check_vip, get_user_by_id_telegram_id, check_admin
from telegram_bot.keyboards import KB_STOP_BOT, KB_START_BOT


def start_user_bot(string_session: str, telegram_id: int, vip_status: int = 0):
    return Popen([executable, PathManager.get("user_bot/main.py"), string_session, f'{telegram_id}', f'{vip_status}'])


def get_main_keyboard(user_id: int, in_process: bool):
    is_vip = check_vip(user_id)
    user = get_user_by_id_telegram_id(user_id)
    kb = deepcopy(KB_STOP_BOT if in_process else KB_START_BOT)
    if check_admin(user_id):
        kb.add(KeyboardButton(text="Admin"))
    if user and user.session:
        kb.add(KeyboardButton(text="Удалить свои данные"))
    if not is_vip:
        kb.add(KeyboardButton(text="Купить полную версию"))
    return kb
