# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-01-24 21:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qbreport', '0021_qbimportfile_notes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='omxorderhistory',
            name='customerID',
        ),
        migrations.RemoveField(
            model_name='omxorderhistory',
            name='firstName',
        ),
        migrations.RemoveField(
            model_name='omxorderhistory',
            name='lastName',
        ),
        migrations.RemoveField(
            model_name='omxorderhistory',
            name='orderDate',
        ),
    ]
