from django import forms
from .models import RetailBloom

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = RetailBloom
        fields = ('retailbloom_Report',)

        widgets = {
            'retailbloom_Report':forms.FileInput(attrs={'class':'Order-Report'}),
        }
