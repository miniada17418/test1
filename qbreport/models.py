from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
from django.core.urlresolvers import reverse

# Create your models here.

class VendorNames(models.Model):
    qbVendorName = models.CharField(max_length=150)
    omxVendorName = models.CharField(max_length=150)

    def __str__(self):
        return self.qbVendorName 
    class Meta:
        verbose_name_plural = 'Vendor Names'

class OMXOrderHistory(models.Model):
    customID = models.CharField(max_length=45)
    orderNumber = models.CharField(max_length=15, null=True)
    itemCode = models.CharField(max_length=16, null=True)
    description = models.CharField(max_length=150, null=True)
    vendorName = models.CharField(max_length=600, null=True)
    dropShipCOG = models.FloatField( null=True)
    qty = models.IntegerField(null=True)
    total = models.FloatField(null=True)

    def __str__(self):
        return self.customID
    class Meta:
        verbose_name_plural = 'OMX Order History'

class QBImportFile(models.Model):
    notes = models.CharField(max_length=25, blank=True, null=True)
    customID = models.CharField(max_length=45)
    invoiceDate = models.DateField(blank=True, null=True)
    vendorName = models.CharField(max_length=45)
    invoiceNumber = models.CharField(max_length=35,null=True, validators=[RegexValidator(r'^\d\d\d\d\d\d-\d\d$')])
    poNumb = models.CharField(max_length=25, null=True, validators=[RegexValidator(r'^\d\d\d\d\d\d-\d\d$')])
    invocieTotal = models.FloatField(blank=True, null=True)
    dropShipFee = models.FloatField(blank=True, null=True)
    shippingFee = models.FloatField(blank=True, null=True)
    omxPO = models.IntegerField(blank=True, null=True)
    omxTotal = models.FloatField(blank=True, null=True)
    totalDifference = models.FloatField(default=None)
    discrepancy = models.CharField(max_length=45, blank=True, null=True)
    memo = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.customID

class UploadFile(models.Model):
    userName = models.ForeignKey('auth.User')
    email = models.EmailField(unique=False)
    orderReport = models.FileField(upload_to='qbreports/uploads/')
    formatedFile = models.FileField(upload_to='qbreports/uploads/', default='qbreports/uploads/test.xlsx')
    uploadDate = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('download_file')

    class Meta:
        verbose_name_plural = 'Uploaded Files'

    def __str__(self):
        return self.orderReport

class NeedToAddVendorToDatabase(models.Model):
    verndorname = models.CharField(max_length=45, blank=True, null=True, unique=True)

    def __str__(self):
        return self.verndorname
