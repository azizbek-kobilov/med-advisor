from aiogram.dispatcher.filters.state import StatesGroup, State


class Wait(StatesGroup):
    WaitAdmin = State()
    WaitSending = State()
    WaitSendingConfirm = State()
