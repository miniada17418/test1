# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-01-04 19:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qbreport', '0015_auto_20180104_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qbimportfile',
            name='invoiceNumber',
            field=models.CharField(max_length=15, null=True),
        ),
    ]