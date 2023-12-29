from apscheduler.schedulers.background import BackgroundScheduler
from reminder.tasks import check_and_send_reminders

scheduler = BackgroundScheduler()

scheduler.add_job(check_and_send_reminders, 'interval', minutes=1)

scheduler.start()
