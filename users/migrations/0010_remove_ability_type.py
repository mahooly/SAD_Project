# Generated by Django 2.0.5 on 2018-07-18 09:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20180714_0249'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ability',
            name='type',
        ),
    ]
