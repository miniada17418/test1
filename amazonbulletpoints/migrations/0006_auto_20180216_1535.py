# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-02-16 21:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('amazonbulletpoints', '0005_auto_20180216_1320'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itemcodetopull',
            old_name='sku',
            new_name='itemCode',
        ),
    ]
