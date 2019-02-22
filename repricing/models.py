from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse

# Create your models here.

class RepricingOMXData(models.Model):
    bfdItemCode = models.CharField(max_length=255,null=True,blank=True)
    vendorID = models.PositiveIntegerField(null=True,blank=True)
    vendorCode = models.CharField(max_length=255,null=True,blank=True)
    vendor_UPC = models.CharField(max_length=16, null=True,blank=True)
    vendor_ProductName = models.CharField(max_length=250, null=True,blank=True)
    currWholesalePrice_AD = models.DecimalField(max_digits=12, decimal_places=2, null=True,blank=True)
    newWholesalePrice_AD = models.DecimalField(max_digits=12, decimal_places=2, null=True,blank=True)
    currWholesalePrice_BD = models.DecimalField(max_digits=12, decimal_places=2, null=True,blank=True)
    newWholesalePrice_BD = models.DecimalField(max_digits=12, decimal_places=2, null=True,blank=True)
    currDropShipPrice_AD = models.DecimalField(max_digits=12, decimal_places=2, null=True,blank=True)
    newDropShipPrice_AD = models.DecimalField(max_digits=12, decimal_places=2, null=True,blank=True)
    currDropShipPrice_BD = models.DecimalField(max_digits=12, decimal_places=2, null=True,blank=True)
    newDropShipPrice_BD = models.DecimalField(max_digits=12, decimal_places=2, null=True,blank=True)
    dropShipFee = models.DecimalField(max_digits=12, decimal_places=2, null=True,blank=True)
    mapPrice = models.DecimalField(max_digits=12, decimal_places=2, null=True,blank=True)
    fullRetailPrice_MSRP = models.DecimalField(max_digits=12, decimal_places=2, null=True,blank=True)
    optionOneValue = models.CharField(max_length=250, null=True,blank=True)
    optionOneSurcharge = models.DecimalField(max_digits=12, decimal_places=2, null=True,blank=True)
    optionTwoValue = models.CharField(max_length=250, null=True,blank=True)
    optionTwoSurcharge = models.DecimalField(max_digits=12, decimal_places=2, null=True,blank=True)
    optionThreeValue = models.CharField(max_length=250, null=True,blank=True)
    optionThreeSurcharge = models.DecimalField(max_digits=12, decimal_places=2, null=True,blank=True)



    def __str__(self):
        return self.vendor_ProductName