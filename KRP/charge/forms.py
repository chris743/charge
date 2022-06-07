from dataclasses import fields
from tkinter.tix import Form
from django.forms import ModelForm
from django import forms
from .models import Commodities, PackagingCosts, BagCost, BagType, Styles, BoxDifference, Packaging

class BagTypeForm(ModelForm):
    class Meta:
        model = BagType
        fields=['bagType', 'description', 'miscCharges']

        widgets = {
            'bagType': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'miscCharges': forms.TextInput(attrs={'class': 'form-control'}),
        }
class PackagingForm(ModelForm):
    class Meta:
        model = PackagingCosts
        fields=['bagType', 'filmCostPerMeter', 'netCostPerMeter', 'vexarClipCost', 'miscCost']

        widgets = {
            'filmCostPerMeter': forms.TextInput(attrs={'class': 'form-control'}),
            'netCostPerMeter': forms.TextInput(attrs={'class': 'form-control'}),
            'vexarClipCost': forms.TextInput(attrs={'class': 'form-control'}),
            'miscCost': forms.TextInput(attrs={'class': 'form-control'}),
        }         

class BagCostForm(ModelForm):
    class Meta:
        model = BagCost
        fields = ['bagType', 'description', 'bagWeight', 'costPerBag', 'bagLength', 'wastePercentage',
        'laborCost', 'totalCost']

        widgets = {
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'bagWeight': forms.TextInput(attrs={'class': 'form-control'}),
            'costPerBag': forms.TextInput(attrs={'class': 'form-control'}),
            'bagLength': forms.TextInput(attrs={'class': 'form-control'}),
            'wastePercentage': forms.TextInput(attrs={'class': 'form-control'}),
            'laborCost': forms.TextInput(attrs={'class': 'form-control'}),
            'totalCost': forms.TextInput(attrs={'class': 'form-control'}),
        }


class StylesForm(ModelForm):
    class Meta:
        model = Styles
        fields = ['commodity', 'bagType', 'twb_flag', 'count', 'bagSize', 'weight', 'flag', 'countSize']

        widgets = {
            'count': forms.TextInput(attrs={'class': 'form-control'}),
            'bagSize': forms.TextInput(attrs={'class': 'form-control'}),
            'weight': forms.TextInput(attrs={'class': 'form-control'}),
            'flag': forms.TextInput(attrs={'class': 'form-control'}),
            'countSize': forms.TextInput(attrs={'class': 'form-control'}),
        }


class CommodityForm(ModelForm):
    class Meta:
        model = Commodities
        fields = [
            'description', 'avgCtnPrice', 'stdCtnCost', 'netWeightChile', 'netWeightDomestic', 'packingCharge',
            'pallets', 'profitPerBag', 'promo'
        ]

        widgets = {
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'avgCtnPrice': forms.TextInput(attrs={'class': 'form-control'}),
            'stdCtnCost': forms.TextInput(attrs={'class': 'form-control'}),
            'netWeightChile': forms.TextInput(attrs={'class': 'form-control'}),
            'netWeightDomestic': forms.TextInput(attrs={'class': 'form-control'}),
            'packingCharge': forms.TextInput(attrs={'class': 'form-control'}),
            'pallets': forms.TextInput(attrs={'class': 'form-control'}),
            'profitPerBag': forms.TextInput(attrs={'class': 'form-control'}),
            'promo': forms.TextInput(attrs={'class': 'form-control'}),
        }

class BoxDifferenceForm(ModelForm):
    class Meta:
        model = BoxDifference
        fields=['name', 'boxDiff', 'description']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'boxDiff': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }

class PackagingForm(ModelForm):
    class Meta:
        model = Packaging
        fields=['description', 'cost']

        widgets = {
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'cost': forms.TextInput(attrs={'class': 'form-control'}),
        }