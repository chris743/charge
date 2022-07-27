from django.shortcuts import render
from charge.models import Commodities, BagType, Styles, BoxDifference
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.core.serializers import serialize


# Create your views here.
class Search(View):
    template_name = 'sales_search/search.html'

    result = ""

    def getCommodities(self):
        commodities = Commodities.objects.all()
        return commodities

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
        fob=params.POST['fob']

        type = BagType.objects.get(description=type_raw).id

        style = Styles.objects.get(commodity=commodity, bagType=type, countSize=count_size)

        def costDomestic(style):
            box_difference = BoxDifference.objects(name=style.bagType).boxDiff
            result = (fob * style.conversionDomestic) + style.totalAdjustment + box_difference
            return result

        data = serialize("json", [style], fields=('commodity', 'countSize', 'costDomestic'))
        return HttpResponse(data, content_type="application/json")
       

    def get(self, request, *args, **kwargs):
        commodityQuery = self.getCommodities()
        ctx = {'commodities': commodityQuery, 'result': self.result}
        return render(request, self.template_name, ctx)
