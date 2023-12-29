from django.contrib import admin
from reminder.models import MedicationReminder


@admin.register(MedicationReminder)
class MedicationReminderAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'user', 'drug_name', 'reminder_time',
                    'duration_days', 'created', 'modified']
    date_hierarchy = 'created'
