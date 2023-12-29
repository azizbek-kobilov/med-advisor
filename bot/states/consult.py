from aiogram.dispatcher.filters.state import StatesGroup, State


class Consult(StatesGroup):
    problem_desc = State()
