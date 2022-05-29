from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('BagTypes/', views.bagType, name="BagTypes" ),
    path('BagCosts/', views.bagCosts, name="BagCosts"),
    path('PkgCosts/', views.pkgCosts, name="pkgCosts")
]