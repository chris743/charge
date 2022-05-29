from django.shortcuts import render
from .models import BoxType, BagCost, PackagingCosts
# Create your views here.
def home(request):
    return render(request, 'charge/home.html')

def bagType(request):
    boxQuery = BoxType.objects.all()

    ctx = {'boxTypes': boxQuery}
    return render(request, 'charge/boxTypes.html', ctx)


def bagCosts(request):
    costQuery = BagCost.objects.all()

    ctx = {'bagCosts': costQuery}
    return render(request, 'charge/bagCosts.html', ctx)

def pkgCosts(request):
    pkgQuery = PackagingCosts.objects.all()

    ctx = {"pkgcosts": pkgQuery}
    return render(request, 'charge/pkgCosts.html', ctx)