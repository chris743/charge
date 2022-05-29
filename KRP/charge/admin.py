from django.contrib import admin
from .models import BoxType, BagCost, PackagingCosts

# Register your models here.
admin.site.register(BoxType)
admin.site.register(BagCost)
admin.site.register(PackagingCosts)