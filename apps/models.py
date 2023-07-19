from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.

class Tata(models.Model):
    title=models.CharField(max_length=50, unique=True)
    slug=models.SlugField(max_length=50, unique=True)
    photo=models.ImageField(upload_to='photo/%y/%m/%d/', blank=True)
    content=RichTextField()

class Useful(models.Model):
    title=models.CharField(max_length=50, unique=True)  
    slug=models.CharField(max_length=50, unique=True)  
    photo=models.ImageField(upload_to='photo/%y/%m/%d/', blank=True)
    content=RichTextField()
