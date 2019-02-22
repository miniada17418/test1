# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-01-11 19:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repricing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RepricingOMXData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendorID', models.PositiveIntegerField(blank=True, null=True)),
                ('vendorCode', models.CharField(blank=True, max_length=255, null=True)),
                ('vendor_UPC', models.CharField(blank=True, max_length=16, null=True)),
                ('vendor_ProductName', models.CharField(blank=True, max_length=250, null=True)),
                ('currWholesalePrice_AD', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('newWholesalePrice_AD', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('currWholesalePrice_BD', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('newWholesalePrice_BD', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('currDropShipPrice_AD', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('newDropShipPrice_AD', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('currDropShipPrice_BD', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('newDropShipPrice_BD', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('dropShipFee', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('mapPrice', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('fullRetailPrice_MSRP', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('optionOneValue', models.CharField(blank=True, max_length=250, null=True)),
                ('optionOneSurcharge', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('optionTwoValue', models.CharField(blank=True, max_length=250, null=True)),
                ('optionTwoSurcharge', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('optionThreeValue', models.CharField(blank=True, max_length=250, null=True)),
                ('optionThreeSurcharge', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
            ],
        ),
    ]
