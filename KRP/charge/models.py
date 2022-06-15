from asyncio.windows_events import NULL
from django.db.models.deletion import CASCADE
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
        print("im here")
        if self.netWeightDomestic == 0:
            return 0
        else:
            print("math time")
            pricePerPound = (self.avgCtnPrice - self.packingCharge) / self.netWeightDomestic
            self.pricePerPound = pricePerPound

    def __str__(self) -> str:
        return self.description

class Styles(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    commodity = models.ForeignKey(Commodities, on_delete=models.CASCADE, default=1)
    bagType = models.ForeignKey(BagType, on_delete=models.CASCADE, default=1)
    referring_bagCost = models.ForeignKey(BagCost, on_delete=models.CASCADE, default=1, db_constraint=False)
    twb_flag = models.BooleanField(null=True, choices=((True,('Yes')),(False, ('No'))))
    count = models.IntegerField(null=False, default=0)
    bagSize = models.IntegerField(null=False, default=0)
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
    def palletsAdjustment(self):
        value = (self.commodity.pallets * self.conversionDomestic)
        nickeld = value *20
        rounded = round(nickeld, 0)
        result = rounded /20
        return round(result, 2)

    @property
    def promoAdjustment(self):
        result = self.commodity.promo * self.conversionDomestic
        return result

    @property
    def packingAdjustment(self):
        if (self.weight > 0):
            value = self.bagType.miscCharges * (self.weight / self.commodity.netWeightDomestic)
            result = self.round_to_value(value)
            return result
        else:
            value = self.count * (self.referring_bagCost.totalCost + self.commodity.profitPerBag)
            value = self.round_to_value(value)
            return value
    
    @property
    def fruitLossAdjustment(self):
        if self.count == 0:
            return NULL
        else:
            result = self.count * .3 * self.commodity.pricePerPound
            result = self.round_to_value(result)
            return result

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
        return 1

class BoxDifference(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    name = models.CharField(null=False, max_length=25)
    boxDiff = models.FloatField(null=False, default=0)
    description = models.CharField(max_length=30)

class Packaging(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    description = models.CharField(max_length=50)
    cost = models.FloatField(null=False, default=0)

    @property
    def boxChargeChile(self):
        result = self.cost + .05
        return result

class LaborCost(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    bagType = models.ForeignKey(BagType, on_delete=models.CASCADE)
    people = models.IntegerField(null=False, default=0)
    bagsPerMinute = models.IntegerField(null=False, default=0)
    wagesPerHour = models.FloatField(null=False, default=0)

    @property
    def laborPerBag(self):
        result = (self.people * self.wagesPerHour) / (self.bagsPerMinute * 60)
        return result

class MiscPackaging(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    description = models.CharField(max_length=50)
    cost = models.FloatField(null=False, default=0)
    boxChargeChile = models.FloatField(null=False, default=0)
