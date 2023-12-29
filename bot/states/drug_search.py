from aiogram.dispatcher.filters.state import StatesGroup, State


class DrugSearch(StatesGroup):
    drug_name = State()
