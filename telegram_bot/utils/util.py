from copy import deepcopy
from aiogram.types import KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from telegram_bot.database.methods.get import get_user_by_id_telegram_id
from telegram_bot.keyboards import KB_STOP_BOT, KB_START_BOT
from telegram_bot.utils.process import check_process


def get_main_keyboard(user_id: int) -> ReplyKeyboardMarkup:
    user = get_user_by_id_telegram_id(user_id)
    kb = deepcopy(KB_STOP_BOT if check_process(user_id) else KB_START_BOT)
    if user and user.session:
        kb.add(KeyboardButton(text="Удалить свои данные ⚠️"))
    kb.add("Узнать комманды 📌")
    if not user.vip and not user.admin:
        kb.add(KeyboardButton(text="Купить полную версию 💸"))
    if not user.admin:
        kb.add("Тех-поддержка ⚙")
    if user and user.admin:
        kb.add(KeyboardButton(text="Admin 🤡"))
    return kb


def get_admin_keyboard(user_id: int) -> InlineKeyboardMarkup:
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
