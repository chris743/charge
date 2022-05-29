from tkinter import CASCADE
import uuid
from django.db import models

# Create your models here.
class BoxType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    boxType = models.CharField(max_length=50, null=True)
    description = models.TextField(null=True)
    miscCharges = models.FloatField(default=0, null=False)

    def __str__(self) -> str:
        return self.boxType

class BagCost(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    boxType = models.ForeignKey(BoxType, on_delete=models.CASCADE, default=1)
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
    boxType = models.ForeignKey(BoxType, on_delete=models.CASCADE, default=1)
    filmCostPerMeter = models.FloatField(null=False, default=0)
    netCostPerMeter = models.FloatField(null=False, default=0)
    vexarClipCost = models.FloatField(null=False, default=0)
    miscCost = models.FloatField(null=False, default=0)


