# Generated by Django 3.2.14 on 2022-12-03 18:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_daily_today'),
    ]

    operations = [
        migrations.AddField(
            model_name='tekst',
            name='opened_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='daily',
            name='today',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 12, 3, 19, 55, 14, 74813)),
        ),
    ]
