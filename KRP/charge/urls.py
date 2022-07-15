from unicodedata import name
from django.urls import path
from . import views, getweights

urlpatterns = [
    path('home/', views.home, name="home"),


    path('bagtypes/', views.bagType, name="BagTypes" ),
    path('updateBagType/<pk>', views.updateBagType, name="updateBagType"),
    path('deleteBagType/<pk>', views.deleteBagType, name="delete-bag-type"),

    path('bagcosts/', views.bagCosts, name="BagCosts"),
    path('updateBagCostEntry/<pk>', views.updateBagCostEntry, name="updateBagCostEntry"),
    path('deleteBagCost/<entry_id>', views.deleteBagCost, name="delete-bag-cost"),

    path('pkgcosts/', views.pkgCosts, name="pkgCosts"),
    path('pkg-delete/<pk>', views.deletePkg, name="delete-pkg"),
    path('update-pkg/<pk>', views.updatePkg, name="update-pkg"),
    
    path('commodities/', views.commodities, name="commodities"),
    path('updateCommodity/<pk>', views.updateCommodity, name="update-commodity"),
    path('deleteCommodity/<pk>', views.deleteCommodity, name="delete-commodity"),

    path('styles/', views.styles, name="styles"),
    path('updateStlye/<pk>', views.updateStyle, name="update-style"),
    path('deleteStyle/<pk>', views.deleteStyle, name="delete-style"),

    path('boxDiff/', views.boxDiff, name="boxDiff"),
    path('update-boxDiff/<pk>', views.update_boxDiff, name="update-boxDiff"),
    path('delete-boxDiff/<pk>', views.delete_boxDiff, name="delete-boxDiff"),

    path('packaging/', views.packaging, name="packaging"),
    path('update-packaging/<pk>', views.update_packaging, name="update-packaging"),
    path('delete-packaging/<pk>', views.delete_packaging, name="delete-packaging"),

    path('laborCosts/', views.laborCosts, name="laborCosts"),
    path('update-laborCosts/<pk>', views.update_laborCosts, name="update-laborCosts"),
    path('delete-laborCosts/<pk>', views.delete_laborCosts, name="delete-laborCosts"),

    path('miscPackaging/', views.miscPackaging, name="miscPackaging"),
    path('update-miscPackaging/<pk>', views.update_miscPackaging, name="update-miscPackaging"),
    path('delete-miscPackaging/<pk>', views.delete_miscPackaging, name="delete-miscPackaging"),

    path('getweights/', views.getWeights, name="getweights"),

    path('reportBuilder/', views.reportBuilder, name="reportBuilder"),
]