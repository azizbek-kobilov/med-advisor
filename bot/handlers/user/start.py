from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from bot.keyboards.default.menu import menu_markup
from bot.models import TelegramUser
from loader import dp
from bot.states import UserRegister


# Команда start
@dp.message_handler(CommandStart(), state="*")
async def start(message: Message, state=FSMContext):
    await state.finish()

    telegram_user, created = TelegramUser.objects.get_or_create(chat_id=message.from_user.id)

    if not telegram_user.phone_number:
        telegram_user.first_name = message.from_user.first_name
        telegram_user.last_name = message.from_user.last_name
        telegram_user.save()
        await message.answer('Введите ваше имя:')
        await UserRegister.name.set()
    else:
        await message.answer(f'<b>{telegram_user.first_name} {telegram_user.last_name}</b>, рады снова видеть вас!',
                             reply_markup=menu_markup())
