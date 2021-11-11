from django import forms
from .models import Ocr 
from .models import Ocr2 
class ImageUpload(forms.ModelForm):
   class Meta:
       model = Ocr 
    #    The field name should be same as database fieldname
       fields = ['image']


# for uploading image to be read with a reference image 
class ImageUpload2(forms.ModelForm):
   class Meta:
       model = Ocr2 
    #    The field names should be same as database fieldnames
       fields = ['image','image2']