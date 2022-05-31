from django.shortcuts import render
from .models import BoxType, BagCost, PackagingCosts, Commodities
from .forms import PackagingForm
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
    form = PackagingForm()

   
    if request.method == 'POST':
        form = PackagingForm(request.POST)
        if form.is_valid():
            form.save()
            form = PackagingForm()

    ctx = {"pkgcosts": pkgQuery, 'form': form,}


    return render(request, 'charge/pkgCosts.html', ctx)



def commodities(request):
    commoditiesQuery = Commodities.objects.all()

    ctx = {'commodities': commoditiesQuery}
    return render(request, 'charge/commodities.html', ctx)