# Generated by Django 3.2.14 on 2022-12-04 20:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20221204_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daily',
            name='today',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 12, 4, 21, 9, 34, 748994)),
        ),
    ]