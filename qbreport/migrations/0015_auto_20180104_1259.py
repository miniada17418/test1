# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-01-04 18:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qbreport', '0014_uploadfile_formatedfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qbimportfile',
            name='invoiceDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='qbimportfile',
            name='paymentDate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
