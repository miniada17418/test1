from django import forms
from .models import ItemCodeToPull

class ItemCodeUploadFile(forms.ModelForm):
    class Meta:
        model = ItemCodeToPull
        fields = ('itemCode',)

        widgets = {
            'itemCode':forms.FileInput(attrs={'class':'itemCode-field'}),
        }
