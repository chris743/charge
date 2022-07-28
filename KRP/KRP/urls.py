
from django.contrib import admin
from django.urls import path, include
from django import views as django_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('data/', include('charge.urls')),
    path('', include('users.urls')),
    path('search/', include('sales_search.urls')),
]
