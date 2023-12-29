from .models import MedicationReminder
from bot.utils import send_telegram_message
import datetime


def check_and_send_reminders():
    now = datetime.datetime.now()
    current_time = now.time()
    current_date = now.date()
    reminders = MedicationReminder.objects.all()

    for reminder in reminders:
        end_date = reminder.created.date() + datetime.timedelta(days=reminder.duration_days)

        if reminder.last_reminder_sent and reminder.last_reminder_sent.date() == current_date:
            continue

        if end_date >= current_date and current_time >= reminder.reminder_time:
            user_chat_id = reminder.user.chat_id
            message = f"Напоминание: время принять ваше лекарство '{reminder.drug_name}'."
            send_telegram_message(user_chat_id, message)

            reminder.last_reminder_sent = now
            reminder.save()

        if current_date > end_date:
            reminder.delete()
