from django.contrib import admin
from .models import Tata, Useful

# Register your models here.
@admin.register(Tata)
class DataAdmin(admin.ModelAdmin):
    list_display=['id', 'title', 'slug', 'photo']
    prepopulated_fields={'slug':('title',)}


@admin.register(Useful) 
class UsefulAdmin(admin.ModelAdmin):
    list_display=['id','title','slug','photo']  
    prepopulated_fields={'slug':('title',)} 