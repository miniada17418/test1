# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-02-08 19:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repricing', '0002_repricingomxdata'),
    ]

    operations = [
        migrations.DeleteModel(
            name='RepricingData',
        ),
    ]
