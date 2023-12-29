from aiogram.types import Message
from aiogram.dispatcher.filters import BoundFilter
from bot.utils import is_admin


class IsAdmin(BoundFilter):
    async def check(self, message: Message):
        return is_admin(message.from_user.id)
