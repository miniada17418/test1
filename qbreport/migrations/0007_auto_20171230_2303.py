# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-12-31 05:03
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('qbreport', '0006_auto_20171230_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfile',
            name='uploadDate',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 31, 5, 3, 40, 827088, tzinfo=utc)),
        ),
    ]
