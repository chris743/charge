from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('bagtypes/', views.bagType, name="BagTypes" ),
    path('bagcosts/', views.bagCosts, name="BagCosts"),
    path('bag-cost-delete/<pk>', views.deleteBagType, name="delete-bag-cost"),
    path('pkgcosts/', views.pkgCosts, name="pkgCosts"),
    path('pkg-delete/<pk>', views.deletePkg, name="delete-pkg"),
    path('update-pkg/<pk>', views.updatePkg, name="update-pkg"),
    path('commodities/', views.commodities, name="commodities"),
    path('deleteEntry/<entry_id>', views.deleteEntry, name="deleteEntry"),
    path('updateBagCostEntry/<pk>', views.updateBagCostEntry, name="updateBagCostEntry"),
    path('updateBagType/<pk>', views.updateBagType, name="updateBagType"),

    path('styles/', views.styles, name="styles")
]