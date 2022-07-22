from django.shortcuts import render, redirect
from charge.models import Commodities, BagType, Styles
from django.http import JsonResponse, HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def search(request):
    commodities = Commodities.objects.all()
    bagTypeQuery = BagType.objects.all()

    ctx = {'commodities': commodities, 'bagType': bagTypeQuery}
    return render(request, 'sales_search/search.html', ctx)

@csrf_exempt
def getBags(params):
    id = params.POST['id']
    types = Styles.objects.filter(commodity=id)
    bagTypes = {}
    i=1
    for type in types:
        bagTypes[i] = type.bagType.description
        i+=1

    return JsonResponse(bagTypes)

@csrf_exempt
def getCountSize(params):
    type = params.POST['type']
    commodity = params.POST['commodity']
    typeQuery = BagType.objects.get(description=type).id

    count_sizes = Styles.objects.filter(bagType=typeQuery, commodity=commodity)
    sizes = {}
    i=1
    for style in count_sizes:
        sizes[i] = style.countSize
        i+=1
    return JsonResponse(sizes)

@csrf_exempt
def getResults(params):
    type_raw=params.POST['type']
    commodity=params.POST['commodity']
    count_size=params.POST['count_size']

    type = BagType.objects.get(description=type_raw).id

    style = Styles.objects.get(commodity=commodity, bagType=type, countSize=count_size)
    ctx={'style': style}
    return redirect('/item/{{style.id}}')

def displayResult(request):
    return HttpResponse("hello")



