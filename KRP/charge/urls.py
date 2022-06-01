from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('bagtypes/', views.bagType, name="BagTypes" ),
    path('bagcosts/', views.bagCosts, name="BagCosts"),
    path('pkgcosts/', views.pkgCosts, name="pkgCosts"),
    path('commodities/', views.commodities, name="commodities"),
    path('deleteEntry/<entry_id>', views.deleteEntry, name="deleteEntry"),
    path('updateBagCostEntry/<entry_id>', views.updateBagCostEntry, name="updateBagCostEntry")
]