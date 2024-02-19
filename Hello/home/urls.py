from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("services/", views.services, name='services'),
    path("contact", views.contact, name='contact'), 
    path("services/IceCream/", views.IceCream, name='IceCream'),
    path("services/waffle/", views.waffle, name='waffle'),
    path("services/Familypack/", views.Familypack, name='Familypack'),
]