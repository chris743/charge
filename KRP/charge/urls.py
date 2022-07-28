from unicodedata import name
from django.urls import path

from . import views, getweights, reporting
from .models import *


urlpatterns = [
    path('home/', views.home, name="home"),


    path('bagtypes/', views.bagType, name="BagTypes" ),
    path('updateBagType/<pk>', views.updateBagType, name="updateBagType"),
    path('deleteBagType/<pk>', views.deleteBagType, name="delete-bag-type"),
    path('report-bagTypes/', reporting.RenderPDF, {'model': BagType, 'template_name': "charge/pdfs/bagTypeReport.html"}, name="bagType-report"),

    path('bagcosts/', views.bagCosts, name="BagCosts"),
    path('updateBagCostEntry/<pk>', views.updateBagCostEntry, name="updateBagCostEntry"),
    path('deleteBagCost/<entry_id>', views.deleteBagCost, name="delete-bag-cost"),
    path('report-bagCosts/', reporting.RenderPDF, {'model': BagCost, 'template_name': "charge/pdfs/bagCostReport.html"}, name="bagCost-report"),

    path('pkgcosts/', views.pkgCosts, name="pkgCosts"),
    path('pkg-delete/<pk>', views.deletePkg, name="delete-pkg"),
    path('update-pkg/<pk>', views.updatePkg, name="update-pkg"),
    path('report-packagingCosts/', reporting.RenderPDF, {'model': PackagingCosts, 'template_name': "charge/pdfs/packagingCostReport.html"}, name="packagingCost-report"),

    
    path('commodities/', views.commodities, name="commodities"),
    path('updateCommodity/<pk>', views.updateCommodity, name="update-commodity"),
    path('deleteCommodity/<pk>', views.deleteCommodity, name="delete-commodity"),
    path('report-commodities/', reporting.RenderPDF, {'model': Commodities, 'template_name': "charge/pdfs/commoditiesReport.html"}, name="commodities-report"),


    path('styles/', views.styles, name="styles"),
    path('updateStyle/<pk>', views.updateStyle, name="update-style"),
    path('deleteStyle/<pk>', views.deleteStyle, name="delete-style"),
    path('report-styles/', reporting.RenderPDF, {'model': Styles, 'template_name': "charge/pdfs/stylesReport.html"}, name="styles-report"),


    path('boxDiff/', views.boxDiff, name="boxDiff"),
    path('update-boxDiff/<pk>', views.update_boxDiff, name="update-boxDiff"),
    path('delete-boxDiff/<pk>', views.delete_boxDiff, name="delete-boxDiff"),
    path('report-boxDiff/', reporting.RenderPDF, {'model': BoxDifference, 'template_name': "charge/pdfs/boxDifferenceReport.html"}, name="boxDiff-report"),


    path('packaging/', views.packaging, name="packaging"),
    path('update-packaging/<pk>', views.update_packaging, name="update-packaging"),
    path('delete-packaging/<pk>', views.delete_packaging, name="delete-packaging"),
    path('report-packaging/', reporting.RenderPDF, {'model': Packaging, 'template_name': "charge/pdfs/packagingReport.html"}, name="packaging-report"),


    path('laborCosts/', views.laborCosts, name="laborCosts"),
    path('update-laborCosts/<pk>', views.update_laborCosts, name="update-laborCosts"),
    path('delete-laborCosts/<pk>', views.delete_laborCosts, name="delete-laborCosts"),
    path('report-laborCosts/', reporting.RenderPDF, {'model': LaborCost, 'template_name': "charge/pdfs/laborCostReport.html"}, name="laborCost-report"),


    path('miscPackaging/', views.miscPackaging, name="miscPackaging"),
    path('update-miscPackaging/<pk>', views.update_miscPackaging, name="update-miscPackaging"),
    path('delete-miscPackaging/<pk>', views.delete_miscPackaging, name="delete-miscPackaging"),
    path('report-miscPackaging/', reporting.RenderPDF, {'model': MiscPackaging, 'template_name': "charge/pdfs/miscPackagingReport.html"}, name="miscPackaging-report"),


    path('getweights/', views.getWeights, name="getweights"),

]
