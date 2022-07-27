from unicodedata import name
from django.urls import path

from .models import *
from . import views

urlpatterns = [
    path('', views.Search.as_view(), name="BagTypes" ),
    path('getBags/', views.Search.getBags, name="getBags"),
    path('getCountSize/', views.Search.getCountSize, name="getCountSize"),
    path('getResults/', views.Search.getResults, name="results"),
    ]