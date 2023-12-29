from django.db.models.signals import post_save
from django.dispatch import receiver
from bot.utils import send_telegram_message
from consultations.models import Response


@receiver(post_save, sender=Response)
def send_response_notification(sender, instance, created, **kwargs):
    if created:
        message = (f'<b>На ваше обращение №{instance.appeal.id} дан ответ:</b>\n\n'
                   f'<i>"{instance.response_text}"</i>')
        user_chat_id = instance.appeal.user.chat_id
        send_telegram_message(user_chat_id, message)


@receiver(post_save, sender=Response)
def send_update_notification(sender, instance, created, **kwargs):
    if not created:
        message = (f'<b>Ответ на ваше обращение №{instance.appeal.id} был обновлен:</b>\n\n'
                   f'<i>"{instance.response_text}"</i>')
        user_chat_id = instance.appeal.user.chat_id
        send_telegram_message(user_chat_id, message)
