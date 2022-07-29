from django.forms import ModelForm
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple

from .models import Commodities, LaborCost, MiscPackaging, PackagingCosts, BagCost, BagType, Styles, BoxDifference, Packaging

class BagTypeForm(ModelForm):
    class Meta:
        model = BagType
        fields=['bagType', 'description', 'miscCharges']

        widgets = {
            'bagType': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'miscCharges': forms.TextInput(attrs={'class': 'form-control'}),
        }
class PackagingCostForm(ModelForm):
    class Meta:
        model = PackagingCosts
        fields=['bagType', 'filmCostPerMeter', 'netCostPerMeter', 'vexarClipCost', 'labelCost']

        widgets = {
            'filmCostPerMeter': forms.TextInput(attrs={'class': 'form-control'}),
            'netCostPerMeter': forms.TextInput(attrs={'class': 'form-control'}),
            'vexarClipCost': forms.TextInput(attrs={'class': 'form-control'}),
            'labelCost': forms.TextInput(attrs={'class': 'form-control'}),
        }         

class BagCostForm(ModelForm):
    class Meta:
        model = BagCost
        fields = ['bagType', 'description', 'bagWeight', 'costPerBag', 'bagLength', 'wastePercentage']

        widgets = {
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'bagWeight': forms.TextInput(attrs={'class': 'form-control'}),
            'costPerBag': forms.TextInput(attrs={'class': 'form-control'}),
            'bagLength': forms.TextInput(attrs={'class': 'form-control'}),
            'wastePercentage': forms.TextInput(attrs={'class': 'form-control'}),

        }


class StylesForm(ModelForm):

    class Meta:
        model = Styles
        
        fields = ['commodity', 'bagType', 'twb_flag', 'count', 'bagSize', 'weight', 'flag', 'miscPackaging']
        widgets = {
            'count': forms.TextInput(attrs={'class': 'form-control'}),
            'bagSize': forms.TextInput(attrs={'class': 'form-control'}),
            'weight': forms.TextInput(attrs={'class': 'form-control'}),
            'flag': forms.TextInput(attrs={'class': 'form-control'}),
            'miscPackaging': forms.Select(attrs={'class': 'form-control'})
            
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
            #'pricePerPound': forms.TextInput(attrs={'class': 'form-control'}),
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
            #'name': forms.TextInput(attrs={'class': 'form-control'}),
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


class LaborCostForm(ModelForm):
    class Meta:
        model = LaborCost
        fields=['bagType', 'people', 'bagsPerMinute', 'wagesPerHour']

        widgets = {
            'people': forms.TextInput(attrs={'class': 'form-control'}),
            'bagsPerMinute': forms.TextInput(attrs={'class': 'form-control'}),
            'wagesPerHour': forms.TextInput(attrs={'class': 'form-control'}),
        }

class MiscPackagingForm(ModelForm):
    class Meta:
        model = MiscPackaging
        fields=['description', 'cost']

        widgets = {
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'cost': forms.TextInput(attrs={'class': 'form-control'}),
            #'boxChargeChile': forms.TextInput(attrs={'class': 'form-control'}),
        }