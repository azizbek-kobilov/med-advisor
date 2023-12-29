from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from aiogram_broadcaster import MessageBroadcaster
from bot.keyboards.default.admin_kb import admin_markup, no, back, sending, yes_no_markup, yes
from bot.keyboards.default.menu import menu_markup
from bot.models import TelegramUser
from bot.utils import is_admin
from loader import dp
from bot.states import Wait
from aiogram.dispatcher.filters.builtin import Command


# Команда admin
@dp.message_handler(Command('admin'), state='*')
async def admin(message: Message):
    if message.chat.type != 'private':
        return

    if is_admin(message.from_user.id):
        await message.answer('<b>Панель администратора:</b>', reply_markup=admin_markup())
        await Wait.WaitAdmin.set()


# Рассылка
@dp.message_handler(text=sending, state=Wait.WaitAdmin)
async def sending(message: Message):
    await message.answer('🔵 Отправьте рассылку')
    await Wait.WaitSending.set()


@dp.message_handler(state=Wait.WaitSending, content_types=types.ContentType.ANY)
async def sending_answer(message: Message, state=FSMContext):
    await state.update_data(text=message)
    await message.answer('Всё верно? Начать рассылку❓', reply_markup=yes_no_markup())
    await Wait.WaitSendingConfirm.set()


@dp.message_handler(text=yes, state=Wait.WaitSendingConfirm)
async def sending_answer_y(message: Message, state=FSMContext):
    data = await state.get_data()
    text = data.get('text')
    users = [user.chat_id for user in TelegramUser.objects.all()]
    users.remove(message.from_user.id)
    await MessageBroadcaster(users, text).run()
    await message.answer('Рассылка завершена !', reply_markup=menu_markup())
    await state.finish()


# Кнопка Нет во всём state
@dp.message_handler(text=no, state=Wait)
async def answer_n(message: Message, state=FSMContext):
    await state.finish()
    await message.answer('С чего начнем?', reply_markup=menu_markup())


# Кнопка Назад
@dp.message_handler(text=back, state=Wait)
async def back_admin(message: Message, state: FSMContext):
    await state.finish()
    await message.answer('С чего начнем?', reply_markup=menu_markup())
