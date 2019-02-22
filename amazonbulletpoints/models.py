from django.db import models

# Create your models here.

class ItemDetail(models.Model):
    yahooID = models.CharField(max_length=200, blank=True, null=True)
    itemCode = models.CharField(max_length=45,blank=True, null=True)
    itemName = models.CharField(max_length=200,blank=True, null=True)
    description =models.CharField(max_length=2000,blank=True, null=True)

    def __str__(self):
        return self.itemName

class ItemCodeToPull(models.Model):
    itemCode = models.CharField(max_length=45)

    def __str__(self):
        return self.sku
