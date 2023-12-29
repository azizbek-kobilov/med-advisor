from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from bot.keyboards.default.menu import menu_markup
from loader import dp


@dp.message_handler(state="*")
async def echo(message: Message, state=FSMContext):
    await state.finish()
    await message.answer('Вы в главном меню, выберите раздел',
                         reply_markup=menu_markup())
