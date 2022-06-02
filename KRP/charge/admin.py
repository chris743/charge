from django.contrib import admin

from .models import BagType, BagCost, PackagingCosts, Commodities, Styles

# Register your models here.
admin.site.register(BagType)
admin.site.register(BagCost)
admin.site.register(PackagingCosts)
admin.site.register(Commodities)
admin.site.register(Styles)