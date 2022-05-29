from dataclasses import fields
from tkinter.tix import Form
from django.forms import ModelForm
from .models import PackagingCosts, BagCost, BoxType

class PackagingForm(ModelForm):
    class Meta:
        model = PackagingCosts
        fields=['boxType', 'filmCostPerMeter', 'netCostPerMeter', 'vexarClipCost', 'miscCost']