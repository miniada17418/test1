from django import forms
from .models import UploadFile

class DocumenUpload(forms.ModelForm):
    class Meta:
        model = UploadFile
        fields = ('orderReport',)
