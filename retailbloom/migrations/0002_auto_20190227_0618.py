# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2019-02-27 06:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retailbloom', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='retailbloom',
            name='retailbloom_Report',
            field=models.FileField(upload_to='retailbloom/uploads/'),
        ),
    ]
