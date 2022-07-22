from unicodedata import name
from django.urls import path

from .models import *
from . import views

urlpatterns = [
    path('', views.search, name="BagTypes" ),
    path('getBags/', views.getBags, name="getBags"),
    path('getCountSize/', views.getCountSize, name="getCountSize"),
    path('getResults/', views.getResults, name="results"),
]