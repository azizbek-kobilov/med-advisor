# Generated by Django 4.1.13 on 2023-12-29 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consultations', '0002_response'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='response',
            options={'ordering': ['-modified'], 'verbose_name': 'Ответ', 'verbose_name_plural': 'Ответы'},
        ),
    ]
