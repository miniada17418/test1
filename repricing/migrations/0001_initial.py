# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-12-11 03:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RepricingData',
            fields=[
                ('vendorID', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('vendorCode', models.CharField(max_length=75)),
                ('vendor_UPC', models.CharField(max_length=16)),
                ('vendor_ProductName', models.CharField(max_length=250)),
                ('currWholesalePrice_AD', models.DecimalField(decimal_places=2, max_digits=12)),
                ('newWholesalePrice_AD', models.DecimalField(decimal_places=2, max_digits=12)),
                ('currWholesalePrice_BD', models.DecimalField(decimal_places=2, max_digits=12)),
                ('newWholesalePrice_BD', models.DecimalField(decimal_places=2, max_digits=12)),
                ('currDropShipPrice_AD', models.DecimalField(decimal_places=2, max_digits=12)),
                ('newDropShipPrice_AD', models.DecimalField(decimal_places=2, max_digits=12)),
                ('currDropShipPrice_BD', models.DecimalField(decimal_places=2, max_digits=12)),
                ('newDropShipPrice_BD', models.DecimalField(decimal_places=2, max_digits=12)),
                ('dropShipFee', models.DecimalField(decimal_places=2, max_digits=12)),
                ('mapPrice', models.DecimalField(decimal_places=2, max_digits=12)),
                ('fullRetailPrice_MSRP', models.DecimalField(decimal_places=2, max_digits=12)),
                ('optionOneCategory', models.CharField(max_length=250)),
                ('optionOneValue', models.CharField(max_length=250)),
                ('optionOneSurcharge', models.DecimalField(decimal_places=2, max_digits=12)),
                ('optionTwoCategory', models.CharField(max_length=250)),
                ('optionTwoValue', models.CharField(max_length=250)),
                ('optionTwoSurcharge', models.DecimalField(decimal_places=2, max_digits=12)),
                ('optionThreeCategory', models.CharField(max_length=250)),
                ('optionThreeValue', models.CharField(max_length=250)),
                ('optionThreeSurcharge', models.DecimalField(decimal_places=2, max_digits=12)),
            ],
        ),
    ]