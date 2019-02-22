# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-12-31 04:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('qbreport', '0004_auto_20171228_1102'),
    ]

    operations = [
        migrations.AddField(
            model_name='qbimportfile',
            name='invoiceDate',
            field=models.DateField(default=datetime.datetime(2017, 12, 31, 4, 46, 27, 897911, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='qbimportfile',
            name='invoiceNumber',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='qbimportfile',
            name='poNumb',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='uploadfile',
            name='uploadDate',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 31, 4, 46, 27, 899415, tzinfo=utc)),
        ),
    ]
