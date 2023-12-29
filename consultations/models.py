from django.db import models
from model_utils.models import TimeStampedModel
from bot.models import TelegramUser


class Appeal(TimeStampedModel):
    user = models.ForeignKey(verbose_name='Пользователь', to='bot.TelegramUser', on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Текст обращения')

    class Meta:
        verbose_name = 'Обращение'
        verbose_name_plural = 'Обращения'
        ordering = ['-created']

    def __str__(self):
        return 'Обращение № ' + str(self.id)


class Response(TimeStampedModel):
    appeal = models.ForeignKey(Appeal, on_delete=models.CASCADE, verbose_name='Обращение')
    responder = models.ForeignKey(TelegramUser, on_delete=models.SET_NULL, null=True, blank=True,
                                  verbose_name='Ответивший')
    response_text = models.TextField(verbose_name='Текст ответа')

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
        ordering = ['-modified']

    def __str__(self) -> str:
        return f'Ответ на обращение № {self.appeal.id}'
