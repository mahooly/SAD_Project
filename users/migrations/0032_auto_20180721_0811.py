# Generated by Django 2.0.5 on 2018-07-21 03:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0031_auto_20180721_0806'),
    ]

    operations = [
        migrations.AddField(
            model_name='benefactorupdatedfields',
            name='image',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='report',
            name='date',
            field=models.DateField(default=datetime.datetime(2018, 7, 21, 8, 11, 34, 427957)),
        ),
        migrations.AlterField(
            model_name='report',
            name='time',
            field=models.TimeField(default=datetime.datetime(2018, 7, 21, 8, 11, 34, 427956)),
        ),
    ]
