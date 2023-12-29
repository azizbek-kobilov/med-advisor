from aiogram.types import ReplyKeyboardMarkup


find_drug = '💊 Найти лекарство'
remind = '⏰ Напомнить о приеме'
consultation = '👩‍⚕️ Консультация с профессионалом'


def menu_markup():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(find_drug, remind)
    markup.add(consultation)
    return markup
