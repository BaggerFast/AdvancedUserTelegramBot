from copy import deepcopy

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

from telegram_bot.utils.process import check_process
from telegram_bot.keyboards.reply import KB_STOP_BOT, KB_START_BOT
from telegram_bot.database.methods.get import get_user_by_telegram_id


def get_main_keyboard(user_id: int) -> ReplyKeyboardMarkup:
    user = get_user_by_telegram_id(user_id)
    kb = deepcopy(KB_STOP_BOT if check_process(user_id) else KB_START_BOT)
    if user and user.session:
        kb.add(KeyboardButton(text="Удалить свои данные ⚠️"))
    kb.add("Узнать команды 📌")
    if not user.vip and not user.admin:
        kb.add(KeyboardButton(text="Купить полную версию 💸"))
    if not user.admin:
        kb.add("Тех-поддержка ⚙")
    if user and user.admin:
        kb.add(KeyboardButton(text="Admin 🤡"))
    return kb


def get_admin_keyboard(user_id: int) -> InlineKeyboardMarkup:
    user = get_user_by_telegram_id(user_id)
    if not user.admin:
        raise Exception()
    kb = InlineKeyboardMarkup(1)
    kb.add(
        InlineKeyboardButton("Добавить администратора ➕", callback_data="add_admin"),
        InlineKeyboardButton(f"Vip {'ВЫКЛ ❌' if user.vip else 'ВКЛ ✅'}", callback_data="vip_switcher"),
        InlineKeyboardButton("Выдать Vip ✨", callback_data="give_vip"),
        InlineKeyboardButton("Аналитика 🤌", callback_data="analytics"),
        InlineKeyboardButton("Рассылка ✉️", callback_data="advertising"),
        InlineKeyboardButton("Выйти ⛔️", callback_data="admin_exit"),
    )
    return kb


def get_payment_keyboard(link: str = '') -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(1)
    if link:
        kb.add(
            InlineKeyboardButton("Оплатить", web_app=WebAppInfo(url=link))
        )
    kb.add(
        InlineKeyboardButton("Проверить оплату", callback_data="check_payment"),
    )
    return kb
