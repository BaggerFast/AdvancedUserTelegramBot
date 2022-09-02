from copy import deepcopy
from sys import executable
from subprocess import Popen
from aiogram.types import KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from misc.path import PathManager
from telegram_bot.database.methods.get import get_user_by_id_telegram_id
from telegram_bot.database.methods.other import is_vip
from telegram_bot.keyboards import KB_STOP_BOT, KB_START_BOT


def start_user_bot(string_session: str, telegram_id: int, vip_status: int = 0):
    return Popen([executable, PathManager.get("user_bot/main.py"), string_session, f'{telegram_id}', f'{vip_status}'])


def get_main_keyboard(user_id: int, in_process: bool):
    vip = is_vip(user_id)
    user = get_user_by_id_telegram_id(user_id)
    kb = deepcopy(KB_STOP_BOT if in_process else KB_START_BOT)
    if user.admin:
        kb.add(KeyboardButton(text="Admin 🤡"))
    if user and user.session:
        kb.add(KeyboardButton(text="Удалить свои данные ⚠️"))
    if not vip and not user.admin:
        kb.add(KeyboardButton(text="Купить полную версию 💸"))
    return kb


def get_admin_keyboard(user_id: int):
    # todo: fix Exception
    user = get_user_by_id_telegram_id(user_id)
    if not user.admin:
        raise Exception
    kb = InlineKeyboardMarkup(1)
    kb.add(
        InlineKeyboardButton("Добавить администратора ➕", callback_data="add_admin"),
        InlineKeyboardButton(f"Vip {'ВКЛ ✅' if user.vip else 'ВЫКЛ ❌'}", callback_data="vip_switcher"),
        InlineKeyboardButton(f"Выдать Vip ✨", callback_data="give_vip"),
        InlineKeyboardButton("Рассылка ✉️", callback_data="advertising"),
        InlineKeyboardButton("Выйти ⛔️", callback_data="admin_exit"),
    )
    return kb
