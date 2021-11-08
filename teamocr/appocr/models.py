from django.db import models

# Create your models here.

# This file is for creating models or databases 

# The name of the database is Ocr 
# The field of the database is 'image' 

# run 'python manage.py makemigrations' 
# run 'python manage.py migrate' 

class Ocr(models.Model):
    image = models.ImageField(upload_to='images/')  