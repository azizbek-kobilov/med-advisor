from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import types
from aiogram.dispatcher import FSMContext
from bot.keyboards.default.menu import menu_markup
from bot.models import TelegramUser
from loader import dp
from bot.states import UserRegister
import phonenumbers


@dp.message_handler(state=UserRegister.name)
async def register(message: types.Message, state: FSMContext):
    await message.answer('Введите фамилию:')
    await state.update_data(name=message.text)
    await UserRegister.next()


@dp.message_handler(state=UserRegister.surname)
async def register(message: types.Message, state: FSMContext):
    await message.answer('Введите ваш номер телефона:',
                         reply_markup=ReplyKeyboardMarkup(
                             resize_keyboard=True,
                             keyboard=[[KeyboardButton(text='Поделиться номером 📲', request_contact=True)]]
                         ))
    await state.update_data(surname=message.text)
    await UserRegister.next()


@dp.message_handler(state=UserRegister.phone_number, content_types=['contact', 'text'])
async def register(message: types.Message, state: FSMContext):
    if message.content_type == 'contact':
        phone_number = message.contact.phone_number
    elif message.content_type == 'text':
        try:
            phone_number = phonenumbers.parse(message.text, None)
            if not phonenumbers.is_valid_number(phone_number):
                raise ValueError('Invalid phone number')
        except Exception as e:
            await message.answer("Пожалуйста, введите корректный номер телефона.")
            return
        phone_number = phonenumbers.format_number(phone_number, phonenumbers.PhoneNumberFormat.E164)
    else:
        return

    data = await state.get_data()

    user = TelegramUser.objects.get(chat_id=message.from_user.id)
    user.first_name = data.get('name')
    user.last_name = data.get('surname')
    user.phone_number = phone_number
    user.save()

    await message.answer('<b>Вы в главном меню, выберите раздел👇</b>',
                         reply_markup=menu_markup())
    await state.finish()
