from unicodedata import name
from django.urls import path

from .models import *
from . import views


urlpatterns = [
    path('', views.search, name="BagTypes" ),
]