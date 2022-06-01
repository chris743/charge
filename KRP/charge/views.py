from django.shortcuts import redirect, render
from .models import BoxType, BagCost, PackagingCosts, Commodities
from .forms import PackagingForm, BagCostForm
# Create your views here.
def home(request):
    return render(request, 'charge/home.html')

def bagType(request):
    boxQuery = BoxType.objects.all()

    ctx = {'boxTypes': boxQuery}
    return render(request, 'charge/boxTypes.html', ctx)


def bagCosts(request):
    costQuery = BagCost.objects.all()

    form = BagCostForm()

    if request.method == 'POST':
        form = BagCostForm(request.POST)
        if form.is_valid():
            form.save()
            form = BagCostForm()


    ctx = {'bagCosts': costQuery, 'form': form}
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


def deleteEntry(request, entry_id):
        entry = BagCost.objects.get(id=entry_id)
        entry.delete()
        return redirect('BagCosts')



def updateBagCostEntry(request, entry_id):
    entry = BagCost.objects.get(id=entry_id)
    updateForm = BagCostForm(instance=entry)

    if request.method == 'POST':
        updateForm = BagCostForm(request.POST, instance=entry)
        if updateForm.is_valid():
            updateForm.save()
            updateForm = BagCostForm()

    ctx = {'updateForm': updateForm}
    return render(request, 'charge/bagCostsForm.html', ctx)