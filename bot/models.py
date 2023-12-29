from django.core.validators import RegexValidator
from django.db import models
from model_utils.models import TimeStampedModel


class TelegramUser(TimeStampedModel):
    chat_id = models.CharField(max_length=20, unique=True, verbose_name='Телеграм ID')
    first_name = models.CharField(max_length=20, default='', blank=True, null=True, verbose_name='Имя')
    last_name = models.CharField(max_length=20, default='', blank=True, null=True, verbose_name='Фамилия')
    phone_number = models.CharField(max_length=20, default='', blank=True, verbose_name='Номер телефона',
                                    validators=[
                                        RegexValidator(r'^\+?\d{11,15}$',
                                                       message='Номер телефона должен быть в формате +9989XXXXXXXX',)
                                    ])
    lang = models.CharField(max_length=2, verbose_name='Язык', default='ru',
                            choices=[
                                ('ru', 'Русский'),
                                ('uz', 'Узбекский'),
                            ])
    roots = models.CharField(max_length=20, verbose_name='Права', default='user',
                             choices=[
                                 ('user', 'User'),
                                 ('admin', 'Admin'),
                             ])

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self) -> str:
        return self.first_name + ' (' + self.phone_number + ')'


class Parameters(models.Model):
    name = models.CharField(max_length=20, verbose_name='Название')
    value = models.CharField(max_length=255, verbose_name='Значение')

    class Meta:
        verbose_name = 'Параметр'
        verbose_name_plural = 'Параметры'

    def __str__(self) -> str:
        return self.name
