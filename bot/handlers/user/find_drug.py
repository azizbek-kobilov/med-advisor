from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove
from bot.states import DrugSearch
from bot.utils import get_drug_info_from_chatgpt
from loader import dp
from bot.keyboards.default.menu import menu_markup, find_drug


# Обработчики лекарств
@dp.message_handler(text=find_drug)
async def process_find_drug(message: Message):
    await message.answer('Введите название лекарства:', reply_markup=ReplyKeyboardRemove())
    await DrugSearch.drug_name.set()


@dp.message_handler(state=DrugSearch.drug_name)
async def process_drug_name(message: Message, state: FSMContext):
    drug_name = message.text
    drug_info = await get_drug_info_from_chatgpt(drug_name)

    await message.answer(drug_info, reply_markup=menu_markup())
    await state.finish()
