# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-02-16 18:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ItemCodeToPull',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='ItemDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yahooID', models.CharField(blank=True, max_length=25, null=True)),
                ('itemCode', models.CharField(max_length=45)),
                ('itemName', models.CharField(max_length=45)),
                ('description', models.CharField(max_length=900)),
            ],
        ),
    ]