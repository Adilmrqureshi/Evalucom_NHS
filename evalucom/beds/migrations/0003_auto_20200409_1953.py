# Generated by Django 3.0.4 on 2020-04-09 19:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('beds', '0002_auto_20200408_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='vacancy_updated',
            field=models.DateField(verbose_name=datetime.datetime(2020, 4, 9, 19, 53, 55, 500740, tzinfo=utc)),
        ),
    ]