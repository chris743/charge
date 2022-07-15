from pickle import TRUE
from tarfile import TarFile
from django.db.models.deletion import CASCADE
import uuid
from django.db import models


# Create your models here.
class BagType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False, max_length=36)
    bagType = models.CharField(max_length=50, null=True)
    description = models.TextField(null=True)
    miscCharges = models.FloatField(default=0, null=False)

    def __str__(self) -> str:
        return self.bagType

class LaborCost(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
    bagType = models.ForeignKey(BagType, on_delete=models.CASCADE)
    people = models.IntegerField(null=False, default=0)
    bagsPerMinute = models.IntegerField(null=False, default=0)
    wagesPerHour = models.FloatField(null=False, default=0)

    @property
    def laborPerBag(self):
        result = (self.people * self.wagesPerHour) / (self.bagsPerMinute * 60)
        return result

class BagCost(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False, max_length=36)
    bagType = models.ForeignKey(BagType, on_delete=models.CASCADE, default=1)
    description = models.TextField(null=True)
    bagWeight = models.FloatField(null=False, default=0)
    costPerBag = models.FloatField(null=False, default=0)
    bagLength = models.FloatField(null=False, default=0)
    wastePercentage = models.FloatField(null=False, default=0)
    
    @property
    def calculation_costPerBag(self):
        if self.bagType.bagType == "Giro":
            netCost = PackagingCosts.objects.get(bagType=self.bagType).netCostPerMeter
            filmCost = PackagingCosts.objects.get(bagType=self.bagType).filmCostPerMeter
            labelCost = PackagingCosts.objects.get(bagType=self.bagType).labelCost

            result = ((filmCost / 100) * (self.bagLength * 2)) + (((netCost / 100) * self.bagLength) + labelCost)
            return round(result, 4)
        elif self.bagType.bagType == "Vexar":
            netCost = PackagingCosts.objects.get(bagType=self.bagType).netCostPerMeter
            clipCost = PackagingCosts.objects.get(bagType=self.bagType).vexarClipCost
            labelCost = PackagingCosts.objects.get(bagType=self.bagType).labelCost
            result = ((netCost / 100) * self.bagLength) + labelCost + clipCost
            return round(result, 4)
        else:
            return self.costPerBag
            
    @property
    def laborCost(self):
        result = LaborCost.objects.get(bagType=self.bagType).laborPerBag
        return result
        
    @property 
    def costFinal(self):
        total = ((self.calculation_costPerBag * (1 + self.wastePercentage)) + LaborCost.objects.get(bagType=self.bagType).laborPerBag)
        return round(total, 4)

class PackagingCosts(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False, max_length=36)
    bagType = models.ForeignKey(BagType, on_delete=models.CASCADE, default=1)
    filmCostPerMeter = models.FloatField(null=False, default=0)
    netCostPerMeter = models.FloatField(null=False, default=0)
    vexarClipCost = models.FloatField(null=False, default=0)
    labelCost = models.FloatField(null=False, default=0)
    miscCost = models.FloatField(null=False, default=0)

class Commodities (models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False, max_length=36)
    description = models.CharField(max_length=30, blank=False)
    avgCtnPrice = models.FloatField(null=False, default=0)
    stdCtnCost = models.FloatField(null=False, default=0)
    pricePerPound = models.FloatField(null=False, default=0)
    netWeightChile = models.FloatField(null=False, default=0)
    netWeightDomestic = models.FloatField(null=False, default=0)
    packingCharge = models.FloatField(null=False, default=0)
    pallets = models.FloatField(null=False, default=0)
    profitPerBag = models.FloatField(null=True, default=0)
    promo = models.FloatField(null=False, default=0)

    def save(self, *args, **kwargs):
        self.calcPricePerPound()
        super().save(*args, **kwargs)

    def calcPricePerPound(self):
        if self.netWeightDomestic == 0:
            return 0
        else:
            pricePerPound = (self.avgCtnPrice - self.packingCharge) / self.netWeightDomestic
            self.pricePerPound = pricePerPound

    def __str__(self) -> str:
        return self.description

class Styles(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False, max_length=36)
    commodity = models.ForeignKey(Commodities, on_delete=models.CASCADE, default=1)
    bagType = models.ForeignKey(BagType, on_delete=models.CASCADE, default=1)
    referring_bagCost = models.ForeignKey(BagCost, on_delete=models.CASCADE, default=1)
    twb_flag = models.BooleanField(null=True, default=False, choices=((True,('True')),(False, ('False'))))
    count = models.IntegerField(null=False, default=0)
    bagSize = models.IntegerField(null=True, blank=True)
    weight = models.FloatField(null=False, default=0)
    flag = models.IntegerField(null=False, default=0)
    countSize = models.CharField(max_length=200, default="NULL")
    domesticSalesCost = models.IntegerField(null=False, default=0)
    chileanSalesCost = models.FloatField(null=False, default=0)
    boxTypes = models.ManyToManyField("BoxDifference")

    def round_to_value(self, number):
        number = round(number, 2)
        number = (number + .025) * 100
        number = round(number, 1)
        number = ((round(number / 5) * 5))/100
        return number

    def save(self, *args, **kwargs):
        self.updateCountSize()
        super().save(*args, **kwargs)

    def updateCountSize(self):
        self.countSize = ("%s x %s" % (self.count, self.bagSize))

    @property
    def conversionDomestic(self):
        if self.weight > 0:
            result = self.weight / self.commodity.netWeightDomestic
            return result
        else:
            result = (self.count * self.bagSize) / self.commodity.netWeightDomestic
            return result

    @property
    def conversionChile(self):
        return 1

    @property
    def palletsAdjustment(self):
        palletCost = MiscPackaging.objects.get(description="Pallet").cost
        if self.twb_flag == False or self.twb_flag == "NULL":
            result = self.commodity.pallets * self.conversionDomestic
            print(result)
            return self.round_to_value(result)
        else:
            return self.round_to_value(palletCost)
            
    @property
    def promoAdjustment(self):
        result = self.commodity.promo * self.conversionDomestic
        return self.round_to_value(result)

    @property
    def packingAdjustment(self):
        if self.weight > 0:
            value = 1 * (self.weight / self.commodity.netWeightDomestic)
            result = self.round_to_value(value)
            return result
        else:
            costObject = BagCost.objects.get(bagType = self.bagType, bagWeight=self.bagSize)
            labor = LaborCost.objects.get(bagType=self.bagType).laborPerBag
            totalCost = ((labor * (1 + costObject.wastePercentage)) + labor)
       
            value = self.count * (totalCost + self.commodity.profitPerBag)
            print(totalCost)
            print("total")
            value = self.round_to_value(value)
            return value
    
    @property
    def fruitLossAdjustment(self):
        if self.count == 0:
            return 1
        else:
            result = self.count * .3 * self.commodity.pricePerPound
            result = self.round_to_value(result)
            return result

    @property
    def totalAdjustment(self):
        totalAdjustment = self.fruitLossAdjustment + self.packingAdjustment + self.palletsAdjustment + self.promoAdjustment
        return round(totalAdjustment, 5)



class BoxDifference(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False, max_length=36)
    name = models.ForeignKey("MiscPackaging", on_delete=models.CASCADE, default=1)
    boxDiff = models.FloatField(null=False, default=0)
    description = models.CharField(max_length=30)

class Packaging(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False, max_length=36)
    description = models.CharField(max_length=50)
    cost = models.FloatField(null=False, default=0)

    @property
    def boxChargeChile(self):
        result = self.cost + .05
        return result

class MiscPackaging(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False, max_length=36)
    description = models.CharField(max_length=50)
    cost = models.FloatField(null=False, default=0)

    @property
    def boxChargeChile(self):
        result = self.cost + .05
        return round(result, 2)
    
    def __str__(self) -> str:
        return self.description
