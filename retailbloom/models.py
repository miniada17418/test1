from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
from django.core.urlresolvers import reverse
# Create your models here.

class RetailBloom(models.Model):
    file_name = models.CharField(max_length=100)
    total_rows = models.IntegerField(null=True)
    uploadDate = models.DateTimeField(default=timezone.now)
    file_location = models.CharField(max_length=100)
    retailbloom_Report = models.FileField(upload_to='retailbloom/uploads/')

    def __str__(self):
        return self.file_name
    class Meta:
        verbose_name_plural = 'Retail Bloom Data'
