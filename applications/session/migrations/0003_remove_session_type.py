# Generated by Django 4.1.1 on 2022-09-18 01:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('session', '0002_repsession_timesession'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='session',
            name='type',
        ),
    ]
