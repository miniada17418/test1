from django import forms
from .models import RepricingOMXData

class VendorIDForm(forms.ModelForm):
    class Meta:
        model = RepricingOMXData
        fields = ('vendorID',)

        widgets = {
            'vendorID':forms.TextInput(attrs={'class':'vendorcss'}),
        }
