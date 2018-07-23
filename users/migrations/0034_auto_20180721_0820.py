# Generated by Django 2.0.5 on 2018-07-21 03:50

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0033_auto_20180721_0818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='benefactor',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, related_name='ben', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='report',
            name='date',
            field=models.DateField(default=datetime.datetime(2018, 7, 21, 8, 20, 5, 263854)),
        ),
        migrations.AlterField(
            model_name='report',
            name='organization',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, related_name='org', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='report',
            name='rateId',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, related_name='rate', to='users.Rate'),
        ),
        migrations.AlterField(
            model_name='report',
            name='time',
            field=models.TimeField(default=datetime.datetime(2018, 7, 21, 8, 20, 5, 263854)),
        ),
        migrations.AlterField(
            model_name='report',
            name='update',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, related_name='updatedfields', to='users.BenefactorUpdatedFields'),
        ),
        migrations.AlterField(
            model_name='report',
            name='wId',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, related_name='weekly', to='users.WeeklySchedule'),
        ),
    ]