# Generated by Django 3.2.14 on 2022-12-06 18:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20221206_1912'),
    ]

    operations = [
        migrations.AddField(
            model_name='tekst',
            name='image2',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='daily',
            name='today',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 12, 6, 19, 25, 2, 356080)),
        ),
        migrations.AlterField(
            model_name='tekst',
            name='code',
            field=models.CharField(default='ptT4mg1V', max_length=300),
        ),
    ]