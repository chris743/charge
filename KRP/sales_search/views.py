from django.shortcuts import render

# Create your views here.

def search(request):
    ctx = {}
    return render(request, 'sales_search/search.html', ctx)