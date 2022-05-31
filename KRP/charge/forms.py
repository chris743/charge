from dataclasses import fields
from tkinter.tix import Form
from django.forms import ModelForm
from django import forms
from .models import PackagingCosts, BagCost, BoxType

class PackagingForm(ModelForm):
    class Meta:
        model = PackagingCosts
        fields=['boxType', 'filmCostPerMeter', 'netCostPerMeter', 'vexarClipCost', 'miscCost']

        widgets = {
            'filmCostPerMeter': forms.TextInput(attrs={'class': 'form-control'}),
            'netCostPerMeter': forms.TextInput(attrs={'class': 'form-control'}),
            'vexarClipCost': forms.TextInput(attrs={'class': 'form-control'}),
            'miscCost': forms.TextInput(attrs={'class': 'form-control'}),
        }
         