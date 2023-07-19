
from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.index),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about')
    
]
