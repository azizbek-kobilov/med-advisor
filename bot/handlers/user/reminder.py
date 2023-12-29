from datetime import datetime
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove
from bot.models import TelegramUser
from bot.states import Remind
from loader import dp
from bot.keyboards.default.menu import menu_markup, remind
from reminder.models import MedicationReminder


@dp.message_handler(text=remind)
async def process_remind_start(message: Message):
    await message.answer("Введите название лекарства:", reply_markup=ReplyKeyboardRemove())
    await Remind.waiting_for_drug_name.set()


@dp.message_handler(state=Remind.waiting_for_drug_name)
async def process_drug_name(message: Message, state: FSMContext):
    await state.update_data(drug_name=message.text)
    await message.answer("Введите время для напоминания (например, 08:30):")
    await Remind.waiting_for_time.set()


@dp.message_handler(state=Remind.waiting_for_time)
async def process_time(message: Message, state: FSMContext):
    try:
        reminder_time = datetime.strptime(message.text, "%H:%M").time()
        await state.update_data(reminder_time=reminder_time)
        await message.answer("На сколько дней установить напоминание?")
        await Remind.waiting_for_duration.set()
    except ValueError:
        await message.answer("Пожалуйста, введите время в правильном формате (например, 08:30).")


@dp.message_handler(state=Remind.waiting_for_duration)
async def process_duration(message: Message, state: FSMContext):
    try:
        duration_days = int(message.text)
        if duration_days <= 0:
            raise ValueError

    except (ValueError, TypeError):
        await message.answer("Пожалуйста, введите количество дней в виде целого числа.")
        return

    user_data = await state.get_data()
    drug_name = user_data['drug_name']
    reminder_time = user_data['reminder_time']

    user = TelegramUser.objects.get(chat_id=message.from_user.id)
    MedicationReminder.objects.create(
        user=user,
        drug_name=drug_name,
        reminder_time=reminder_time,
        duration_days=duration_days
    )

    await message.answer(
        f"Напоминание для лекарства '{drug_name}' установлено на {reminder_time} на {duration_days} дней.",
        reply_markup=menu_markup())
    await state.finish()
