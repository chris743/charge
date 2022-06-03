from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import BagType, BagCost, BoxDifference, PackagingCosts, Commodities, Styles, Packaging
from .forms import PackagingForm, BagCostForm,StylesForm, BagTypeForm, CommodityForm, BoxDifferenceForm
# Create your views here.
def home(request):
    return render(request, 'charge/home.html')

#-------------BAG TYPE FUNCTIONS---------------
def bagType(request):
    form = BagTypeForm()
    bagQuery = BagType.objects.all()

    if request.method == 'POST':
        form = BagTypeForm(request.POST)
        if form.is_valid():
            form.save()
            form = BagTypeForm()

            
    ctx = {'bagTypes': bagQuery, 'form': form}
    return render(request, 'charge/bagTypes.html', ctx)

def deleteBagType(request, pk):
    entry = BagType.objects.get(id=pk)
    entry.delete()
    return redirect('BagTypes')

def updateBagType(request, pk):
    entry = BagType.objects.get(id=pk)
    form = BagTypeForm(instance=entry)

    if request.method == 'POST':
        form = BagTypeForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('BagTypes')

    ctx = {'form': form}
    return render(request, 'charge/bagTypeForm.html', ctx)

#------------BAG COSTING FUNCTIONS---------------
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

def deleteBagCost(request, entry_id):
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

#--------------PACKAGING FUNCTIONS---------------
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

#---------------Commodities Functions--------------
def commodities(request):
    commoditiesQuery = Commodities.objects.all()
    form = CommodityForm()

    if request.method == 'POST':
        form=CommodityForm(request.POST)
        if form.is_valid():
            form.save()
            form = CommodityForm()

    ctx = {'commodities': commoditiesQuery, 'form': form}
    return render(request, 'charge/commodities.html', ctx)

def updateCommodity(request, pk):
    entry = Commodities.objects.get(id=pk)
    form = CommodityForm(instance=entry)

    if request.method == 'POST':
        form = CommodityForm(request.POST, instance=entry)
        if form.is_valid:
            form.save()
            return redirect('commodities')

    ctx = {'form': form}
    return render(request, 'charge/commoditiesForm.html', ctx)

def deleteCommodity(request,pk):
    entry = Commodities.objects.get(id=pk)
    entry.delete()
    return redirect('commodities')
#--------------Styles Functions--------------------
def styles(request):
    stylesQuery = Styles.objects.all()
    form = StylesForm()

    if request.method == 'POST':
        form = StylesForm(request.POST)
        if form.is_valid():
            form.save()
            form = StylesForm()
            HttpResponseRedirect('charge/styles.html')

    ctx = {'styles': stylesQuery, 'form': form}
    return render(request, 'charge/styles.html', ctx)

def updateStyle(request, pk):
    entry = Styles.objects.get(id=pk)
    form = StylesForm(instance=entry)

    if request.method == 'POST':
        form = StylesForm(request.POST, instance=entry)
        if form.is_valid:
            form.save()
            return redirect('styles')

    ctx = {'form': form}
    return render(request, 'charge/stylesForm.html', ctx)

def deleteStyle(request,pk):
    entry = Styles.objects.get(id=pk)
    entry.delete()
    return redirect('styles')

#-------------Box Difference Functions--------------

def boxDiff(request):
    boxDiffQuery = BoxDifference.objects.all()
    form = BoxDifferenceForm()

    if request.method == 'POST':
        form = BoxDifferenceForm(request.POST)
        form.save()
        form = BoxDifferenceForm()

    ctx = {'boxDiffs': boxDiffQuery, 'form': form}
    return render(request, 'charge/boxDiff.html', ctx)


def update_boxDiff(request, pk):
    entry = BoxDifference.objects.get(id=pk)
    form = BoxDifferenceForm(instance=entry)

    if request.method == 'POST':
        form = BoxDifferenceForm(request.POST, instance=entry)
        if form.is_valid:
            form.save()
            return redirect('boxDiff')

    ctx = {'form': form}
    return render(request, 'charge/boxDiffForm.html', ctx)

def delete_boxDiff(request,pk):
    entry = BoxDifference.objects.get(id=pk)
    entry.delete()
    return redirect('boxDiff')


#---------------Packaging Functions-----------------
def packaging(request):
    packagingQuery = Packaging.objects.all()
    form = PackagingForm()

    if request.method == 'POST':
        form = PackagingForm(request.POST)
        form.save()
        form = PackagingForm()

    ctx = {'packaging': packagingQuery, 'form': form}
    return render(request, 'charge/packaging.html', ctx)


def update_packaging(request, pk):
    entry = Packaging.objects.get(id=pk)
    form = PackagingForm(instance=entry)

    if request.method == 'POST':
        form = PackagingForm(request.POST, instance=entry)
        if form.is_valid:
            form.save()
            return redirect('packaging')

    ctx = {'form': form}
    return render(request, 'charge/packaging.html', ctx)

def delete_packaging(request, pk):
    entry = Packaging.objects.get(id=pk)
    entry.delete()
    return redirect('packaging')

