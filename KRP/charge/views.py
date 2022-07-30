import json
from django.db import DEFAULT_DB_ALIAS
from django.views.generic import ListView
from unicodedata import name
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, FileResponse
from django.shortcuts import redirect, render
from .models import BagType, BagCost, BoxDifference, LaborCost, PackagingCosts, Commodities, Styles, Packaging, MiscPackaging
from .forms import MiscPackaging, PackagingForm, BagCostForm,StylesForm, BagTypeForm, CommodityForm, BoxDifferenceForm, PackagingCostForm, LaborCostForm, MiscPackagingForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import get_template
from django.contrib.admin.utils import NestedObjects

# Create your views here.
@user_passes_test(lambda u: u.is_staff, login_url="denied")
def home(request):
    return render(request, 'charge/home.html')

#-------------BAG TYPE FUNCTIONS---------------
@user_passes_test(lambda u: u.is_staff, login_url="denied")
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

@user_passes_test(lambda u: u.is_staff, login_url="denied")
def deleteBagType(request, pk):
    entry = BagType.objects.get(id=pk)
    entry.delete()
    return redirect('BagTypes')

@user_passes_test(lambda u: u.is_staff, login_url="denied")
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
@user_passes_test(lambda u: u.is_staff, login_url="denied")
def bagCosts(request):
    costQuery = BagCost.objects.all()
    
    form = BagCostForm()

    if request.method == 'POST':
        form = BagCostForm(request.POST)
        if form.is_valid():
            form.save()
            form = BagCostForm()
            HttpResponseRedirect('charge/bagCosts.html')
        else:
            messages.error(request, "Item failed to post to database. Does this bag type have an associated labor cost?")


    ctx = {'bagCosts': costQuery, 'form': form}
    return render(request, 'charge/bagCosts.html', ctx)

@user_passes_test(lambda u: u.is_staff, login_url="denied")
def deleteBagCost(request, entry_id):
        entry = BagCost.objects.get(id=entry_id)
        entry.delete()
        return redirect('BagCosts')

@user_passes_test(lambda u: u.is_staff, login_url="denied")
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

#--------------PACKAGING FUNCTIONS-------------
@user_passes_test(lambda u: u.is_staff, login_url="denied")
def pkgCosts(request):
    pkgQuery = PackagingCosts.objects.all()
    form = PackagingCostForm()

   
    if request.method == 'POST':
        form = PackagingCostForm(request.POST)
        if form.is_valid():
            form.save()
            form = PackagingCostForm()
            HttpResponseRedirect("charge/pkgCost.html")

    ctx = {"pkgcosts": pkgQuery, 'form': form,}


    return render(request, 'charge/pkgCosts.html', ctx)

@user_passes_test(lambda u: u.is_staff, login_url="denied")
def deletePkg(request, pk):
    entry = PackagingCosts.objects.get(id=pk)
    entry.delete()
    return redirect('pkgCosts')

@user_passes_test(lambda u: u.is_staff, login_url="denied")
def updatePkg(request, pk):
    entry = PackagingCosts.objects.get(id=pk)
    form = PackagingCostForm(instance=entry)

    if request.method == 'POST':
        form = PackagingCostForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('pkgCosts')
    ctx = {'form': form}
    return render(request, 'charge/pkgCostForm.html', ctx)

#---------------Commodities Functions--------------
@user_passes_test(lambda u: u.is_staff, login_url="denied")
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

@user_passes_test(lambda u: u.is_staff, login_url="denied")
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

@user_passes_test(lambda u: u.is_staff, login_url="denied")
def deleteCommodity(request,pk):
    entry = Commodities.objects.get(id=pk)
    entry.delete()
    return redirect('commodities')



#--------------Styles Functions--------------------
@user_passes_test(lambda u: u.is_staff, login_url="denied")
def styles(request):
    stylesQuery = Styles.objects.all()

    form = StylesForm()

    if request.method == 'POST':
        form = StylesForm(request.POST)
        bagSize = float(request.POST['size'])
        if form.is_valid():
            newStyle = form.save(commit=False)
            newStyle.bagSize = bagSize
            newStyle.save()
            form = StylesForm()
            HttpResponseRedirect('charge/styles.html')
        else:
            print(form.errors.as_data())

    ctx = {'styles': stylesQuery, 'form': form}
    return render(request, 'charge/styles.html', ctx)

import pandas as pd

@user_passes_test(lambda u: u.is_staff, login_url="denied")
def updateStyle(request, pk):
    entry = Styles.objects.get(id=pk)
    form = StylesForm(instance=entry)

    packagingItems = entry.miscPackaging.all()

    boxDiffs = BoxDifference.objects.all()

    mp_data = {'id':[], 'name':[]}
    mp = pd.DataFrame(mp_data)

    for i in boxDiffs:
        mp.loc[len(mp.index)] = [i.name.id, i.name]
    print(mp)

    data1 = {
            'name':[],
            'cost':[],
            'boxDiff':[]
        }
    
    df = pd.DataFrame(data1)

    for p in packagingItems:
        diff = boxDiffs.get(name=p.id).boxDiff
        df.loc[len(df.index)]=([p.description, p.cost, diff])
        
    print(df)

    if request.method == 'POST':
        bagSize = float(request.POST['size'])
        form = StylesForm(request.POST, instance=entry)
        if form.is_valid():
            newStyle = form.save(commit=False)
            newStyle.bagSize = bagSize
            newStyle.save()
            return HttpResponseRedirect(pk)

    ctx = {'form': form, 'style':entry, 'miscPackaging': df, 'mp_all': mp}
    return render(request, 'charge/stylesForm.html', ctx)



@user_passes_test(lambda u: u.is_staff, login_url="denied")
def deleteStyle(request,pk):
    entry = Styles.objects.get(id=pk)
    entry.delete()
    return redirect('styles')

def delete_related(request, style, pk):
        entry = Styles.objects.get(id=style)
        mp = MiscPackaging.objects.get(description=pk).id
        packagingItem = entry.miscPackaging.get(id=mp)

        entry.miscPackaging.remove(packagingItem)
        return redirect(f'/data/updateStyle/{style}')
        




#-------------Box Difference Functions-----------------
@user_passes_test(lambda u: u.is_staff, login_url="denied")
def boxDiff(request):
    boxDiffQuery = BoxDifference.objects.all()
    form = BoxDifferenceForm()

    if request.method == 'POST':
        form = BoxDifferenceForm(request.POST)
        form.save()
        form = BoxDifferenceForm()

    ctx = {'boxDiffs': boxDiffQuery, 'form': form}
    return render(request, 'charge/boxDiff.html', ctx)

@user_passes_test(lambda u: u.is_staff, login_url="denied")
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

@user_passes_test(lambda u: u.is_staff, login_url="denied")
def delete_boxDiff(request,pk):
    entry = BoxDifference.objects.get(id=pk)
    entry.delete()
    return redirect('boxDiff')


#---------------Packaging Functions-----------------
@user_passes_test(lambda u: u.is_staff, login_url="denied")
def packaging(request):
    packagingQuery = Packaging.objects.all()
    form = PackagingForm()

    if request.method == 'POST':
        form = PackagingForm(request.POST)
        form.save()
        form = PackagingForm()

    ctx = {'packaging': packagingQuery, 'form': form}
    return render(request, 'charge/packaging.html', ctx)

@user_passes_test(lambda u: u.is_staff, login_url="denied")
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

@user_passes_test(lambda u: u.is_staff, login_url="denied")
def delete_packaging(request, pk):
    entry = Packaging.objects.get(id=pk)
    entry.delete()
    return redirect('packaging')


#-----------Labor Cost functions------------

@user_passes_test(lambda u: u.is_staff, login_url="denied")
def laborCosts(request):
    laborQuery = LaborCost.objects.all()
    form = LaborCostForm()

    if request.method == 'POST':
        form = LaborCostForm(request.POST)
        form.save()
        form = LaborCostForm()

    ctx = {'laborCosts': laborQuery, 'form': form}
    return render(request, 'charge/laborCosts.html', ctx)

@user_passes_test(lambda u: u.is_staff, login_url="denied")
def update_laborCosts(request, pk):
    entry = LaborCost.objects.get(id=pk)
    form = LaborCostForm(instance=entry)

    if request.method == 'POST':
        form = LaborCostForm(request.POST, instance=entry)
        if form.is_valid:
            form.save()
            return redirect('laborCosts')

    ctx = {'form': form}
    return render(request, 'charge/laborCosts.html', ctx)

@user_passes_test(lambda u: u.is_staff, login_url="denied")
def delete_laborCosts(request, pk):
    entry = LaborCost.objects.get(id=pk)
    entry.delete()
    return redirect('laborCosts')

#-----------------Misc Packaging Functions-------------------
@user_passes_test(lambda u: u.is_staff, login_url="denied")
def miscPackaging(request):
    packagingQuery = MiscPackaging.objects.all()
    form = MiscPackagingForm()

    if request.method == 'POST':
        form = MiscPackagingForm(request.POST)
        form.save()
        form = MiscPackagingForm()

    ctx = {'miscPackaging': packagingQuery, 'form': form}
    return render(request, 'charge/miscPackaging.html', ctx)

@user_passes_test(lambda u: u.is_staff, login_url="denied")
def update_miscPackaging(request, pk):
    entry = MiscPackaging.objects.get(id=pk)
    form = MiscPackagingForm(instance=entry)

    if request.method == 'POST':
        form = MiscPackagingForm(request.POST, instance=entry)
        if form.is_valid:
            form.save()
            return redirect('miscPackaging')

    ctx = {'form': form}
    return render(request, 'charge/miscPackaging.html', ctx)

@user_passes_test(lambda u: u.is_staff, login_url="denied")
def delete_miscPackaging(request, pk):
    entry = MiscPackaging.objects.get(id=pk)
    entry.delete()
    return redirect('miscPackaging')

@csrf_exempt
def getWeights(params):
    id = params.POST['id']
    costs = BagCost.objects.filter(bagType=id)
    weight = {}
    i=1
    for bag in costs:
        weight[i] = bag.bagWeight
        i+=1

    return JsonResponse(weight)

@csrf_exempt
def updateStyleRelation(params):
    mp = params.POST['miscPackaging_v']
    pk = params.POST['styleid']

    entry = Styles.objects.get(id=pk)
    entry.miscPackaging.add(mp)
    return redirect(f'/data/updateStyle/{pk}')
