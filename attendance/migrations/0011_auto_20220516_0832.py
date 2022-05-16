# Generated by Django 3.2.13 on 2022-05-16 08:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0010_auto_20220516_0708'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='location',
            field=models.CharField(choices=[('client location', 'CLIENT LOCATION'), ('office', 'OFFICE'), ('on duty', 'ON DUTY'), ('Work from home', 'WORK FROM HOME')], default='office', max_length=20),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 16, 8, 32, 48, 43123, tzinfo=utc)),
        ),
    ]
