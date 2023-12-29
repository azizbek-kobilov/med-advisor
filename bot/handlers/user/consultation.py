from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove
from bot.models import TelegramUser
from bot.states import Consult
from consultations.models import Appeal
from loader import dp
from bot.keyboards.default.menu import menu_markup, consultation


# Обработчики консультации
@dp.message_handler(text=consultation)
async def process_consultation(message: Message):
    await message.answer('Опишите вашу проблему или вопрос:', reply_markup=ReplyKeyboardRemove())
    await Consult.problem_desc.set()


@dp.message_handler(state=Consult.problem_desc)
async def process_problem_desc(message: Message, state: FSMContext):
    problem_desc = message.text
    user = TelegramUser.objects.get(chat_id=message.from_user.id)
    appeal = Appeal.objects.create(user=user, text=problem_desc)

    await message.answer(f'Ваше обращение <b>№ {appeal.id}</b> принято. Мы ответим Вам в ближайшее время!',
                         reply_markup=menu_markup())
    await state.finish()
