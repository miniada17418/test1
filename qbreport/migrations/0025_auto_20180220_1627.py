# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-02-20 16:27
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qbreport', '0024_auto_20180220_0615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qbimportfile',
            name='invoiceNumber',
            field=models.CharField(max_length=35, null=True, validators=[django.core.validators.RegexValidator('^\\d\\d\\d\\d\\d\\d-\\d\\d$')]),
        ),
        migrations.AlterField(
            model_name='qbimportfile',
            name='poNumb',
            field=models.CharField(max_length=25, null=True, validators=[django.core.validators.RegexValidator('^\\d\\d\\d\\d\\d\\d-\\d\\d$')]),
        ),
    ]
