# Generated by Django 4.1.13 on 2023-12-29 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reminder', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicationreminder',
            name='duration_days',
            field=models.IntegerField(default=0, verbose_name='Длительность приема (дни)'),
            preserve_default=False,
        ),
    ]