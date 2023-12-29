from django.db import models
from model_utils.models import TimeStampedModel


class MedicationReminder(TimeStampedModel):
    user = models.ForeignKey(verbose_name='Пользователь', to='bot.TelegramUser', on_delete=models.CASCADE)
    drug_name = models.CharField(max_length=100, verbose_name='Название лекарства')
    reminder_time = models.TimeField(verbose_name='Время напоминания')
    duration_days = models.IntegerField(verbose_name='Длительность приема (дни)')
    last_reminder_sent = models.DateTimeField(null=True, blank=True, verbose_name='Последнее напоминание')

    class Meta:
        verbose_name = 'Напоминание'
        verbose_name_plural = 'Напоминания'
        ordering = ['-created']

    def __str__(self):
        return f'Напоминание: {self.drug_name} в {self.reminder_time}'
