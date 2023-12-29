from aiogram.dispatcher.filters.state import StatesGroup, State


class Remind(StatesGroup):
    waiting_for_drug_name = State()
    waiting_for_time = State()
    waiting_for_duration = State()
