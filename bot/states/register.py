from aiogram.dispatcher.filters.state import StatesGroup, State


class UserRegister(StatesGroup):
    language = State()
    name = State()
    surname = State()
    phone_number = State()
