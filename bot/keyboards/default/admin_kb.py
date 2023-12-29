from aiogram.types import ReplyKeyboardMarkup


sending = '📨 Рассылка'
back = '↩ Назад'


def admin_markup():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(sending)
    markup.add(back)
    return markup


yes = '✅ Да'
no = '❌ Нет'


def yes_no_markup():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(yes, no)
    return markup
