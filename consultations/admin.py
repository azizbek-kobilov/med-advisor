from django.contrib import admin
from consultations.models import Appeal, Response


@admin.register(Appeal)
class AppealAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'user', 'created', 'modified']
    date_hierarchy = 'created'


@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'appeal', 'responder', 'created', 'modified']
    date_hierarchy = 'created'
