from django.contrib import admin
from .models import TelegramUser, Parameters


@admin.register(TelegramUser)
class TelegramUserAdmin(admin.ModelAdmin):
    list_display = ['chat_id', 'first_name', 'last_name', 'phone_number', 'roots']
    date_hierarchy = 'created'


@admin.register(Parameters)
class ParametersAdmin(admin.ModelAdmin):
    list_display = ['name', 'value']
