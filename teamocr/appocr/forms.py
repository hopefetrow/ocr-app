from django import forms
from .models import Ocr 

class ImageUpload(forms.ModelForm):
   class Meta:
       model = Ocr 
    #    The field name should be same as database fieldname
       fields = ['image']