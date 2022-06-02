from django.shortcuts import redirect, render
from .models import BagType, BagCost, PackagingCosts, Commodities, Styles
from .forms import PackagingForm, BagCostForm,StylesForm, BagTypeForm
# Create your views here.
def home(request):
    return render(request, 'charge/home.html')

def bagType(request):
    bagQuery = BagType.objects.all()

    ctx = {'bagTypes': bagQuery}
    return render(request, 'charge/bagTypes.html', ctx)

def updateBagType(request, pk):
    entry = BagType.objects.get(id=pk)
    form = BagTypeForm(instance=entry)

    if request.method == 'POST':
        form = BagTypeForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('BagCosts')

    ctx = {'form': form}
    return render(request, 'charge/bagTypeForm.html', ctx)

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

def deleteBagType(request, pk):
    entry = BagCost.objects.get(id=pk)
    entry.delete()
    return redirect('BagCosts')

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

def deletePkg(request, pk):
    entry = PackagingCosts.objects.get(id=pk)
    entry.delete()
    return redirect('pkgCosts')

def updatePkg(request, pk):
    entry = PackagingCosts.objects.get(id=pk)
    form = PackagingForm(instance=entry)

    if request.method == 'POST':
        form = PackagingForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('pkgCosts')
    ctx = {'form': form}
    return render(request, 'charge/pkgCostForm.html', ctx)

def commodities(request):
    commoditiesQuery = Commodities.objects.all()

    ctx = {'commodities': commoditiesQuery}
    return render(request, 'charge/commodities.html', ctx)

def deleteEntry(request, entry_id):
        entry = BagCost.objects.get(id=entry_id)
        entry.delete()
        return redirect('BagCosts')

def updateBagCostEntry(request, pk):
    entry = BagCost.objects.get(id=pk)
    form = BagCostForm(instance=entry)

    if request.method == 'POST':
        form = BagCostForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('BagCosts')

    ctx = {'form': form}
    return render(request, 'charge/bagCostsForm.html', ctx)

def styles(request):
    stylesQuery = Styles.objects.all()
    form = StylesForm()

    if request.method == 'POST':
        form = StylesForm(request.POST)
        if form.is_valid():
            form.save()
            form = StylesForm()

    ctx = {'styles': stylesQuery, 'form': form}
    return render(request, 'charge/styles.html', ctx)