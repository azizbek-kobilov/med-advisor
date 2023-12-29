import requests
from django.conf import settings


def send_telegram_message(chat_id, message):
    token = settings.BOT_TOKEN
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "HTML"
    }
    requests.post(url, data=data)
