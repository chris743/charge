from tkinter import CASCADE
import uuid
from django.db import models


# Create your models here.
class BagType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    bagType = models.CharField(max_length=50, null=True)
    description = models.TextField(null=True)
    miscCharges = models.FloatField(default=0, null=False)

    def __str__(self) -> str:
        return self.bagType

class BagCost(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    bagType = models.ForeignKey(BagType, on_delete=models.CASCADE, default=1)
    description = models.TextField(null=True)
    bagWeight = models.FloatField(null=False, default=0)
    costPerBag = models.FloatField(null=False, default=0)
    bagLength = models.FloatField(null=False, default=0)
    wastePercentage = models.FloatField(null=False, default=0)
    laborCost = models.FloatField(null=False, default=0)
    totalCost = models.FloatField(null=False, default=0)

    @property 
    def costFinal(self):
        total = self.costPerBag * (1 + self.wastePercentage) + self.laborCost
        return total

class PackagingCosts(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    bagType = models.ForeignKey(BagType, on_delete=models.CASCADE, default=1)
    filmCostPerMeter = models.FloatField(null=False, default=0)
    netCostPerMeter = models.FloatField(null=False, default=0)
    vexarClipCost = models.FloatField(null=False, default=0)
    miscCost = models.FloatField(null=False, default=0)

class Commodities (models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    description = models.CharField(max_length=30, blank=False)
    avgCtnPrice = models.FloatField(null=False, default=0)
    stdCtnCost = models.FloatField(null=False, default=0)
    netWeightChile = models.FloatField(null=False, default=0)
    netWeightDomestic = models.FloatField(null=False, default=0)
    packingCharge = models.FloatField(null=False, default=0)
    pallets = models.FloatField(null=False, default=0)
    profitPerBag = models.FloatField(null=False, default=0)
    promo = models.FloatField(null=False, default=0)

    @property
    def pricePerPound(self):
        pricePerPound = (self.avgCtnPrice - self.packingCharge) / self.netWeightDomestic
        return pricePerPound

    def __str__(self) -> str:
        return self.description

class Styles(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    commodity = models.ForeignKey(Commodities, on_delete=models.CASCADE, default=1)
    bagType = models.ForeignKey(BagType, on_delete=models.CASCADE, default=1)
    referring_bagCost = models.ForeignKey(BagCost, on_delete=models.CASCADE, default=1, db_constraint=False)
    twb_flag = models.BooleanField(null=True)
    count = models.IntegerField(null=False, default=0)
    bagSize = models.IntegerField(null=False, default=0)
    weight = models.FloatField(null=False, default=0)
    flag = models.IntegerField(null=False, default=0)
    countSize = models.CharField(max_length=200)
    domesticSalesCost = models.IntegerField(null=False, default=0)
    chileanSalesCost = models.FloatField(null=False, default=0)

    @property
    def palletsAdjustment(self):
        value = (self.commodity.pallets * self.conversionDomestic)
        nickeld = value *20
        rounded = round(nickeld, 0)
        result = rounded /20
        return round(result, 2)

    @property
    def promoAdjustment(self):
        if (self.weight > 0):
            result = round(self.commodity.promo / self.commodity.netWeightDomestic / self.weight, 2)
        else:
            result = round(self.commodity.promo * self.conversionDomestic)

        return result

    @property
    def packingAdjustment(self):
        if (self.weight > 0):
            value = self.bagType.miscCharges * (self.weight / self.commodity.netWeightDomestic)
        else:
            value = self.count *(self.referring_bagCost.costFinal + self.commodity.profitPerBag)

        nickeled = value * 20
        rounded = round(nickeled, 0)
        result = rounded / 20
        return round(result, 2)
    
    @property
    def fruitLossAdjustment(self):
        result = self.count * .3 * self.commodity.pricePerPound
        return round(result, 2)

    @property
    def totalAdjustment(self):
        totalAdjustment = self.fruitLossAdjustment + self.packingAdjustment + self.palletsAdjustment + self.promoAdjustment
        return round(totalAdjustment, 2)

    @property
    def conversionDomestic(self):
        if self.weight > 0:
            result = self.commodity.netWeightDomestic

        else:
            result = (self.referring_bagCost.bagWeight * self.count) / self.commodity.netWeightDomestic
        
        return result

    @property
    def conversionChile(self):
        if self.weight > 0:
            temp = self.commodity.netWeightChile
            result = (self.weight / temp)
        else:
            result = ((self.referring_bagCost.bagWeight * self.count) / self.commodity.netWeightChile)
        
        return round(result,2)

class BoxDifference(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    name = models.CharField(null=False, max_length=25)
    boxDiff = models.FloatField(null=False, default=0)
    description = models.CharField(max_length=30)