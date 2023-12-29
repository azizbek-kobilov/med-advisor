from bot.models import TelegramUser


# Проверка на Админа
def is_admin(id):
    user = TelegramUser.objects.get(chat_id=id)
    return user.roots == 'admin'
