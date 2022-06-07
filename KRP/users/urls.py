from django.urls import path
from . import views

urlpatterns = [


    path('', views.profiles, name="profiles"),

    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),


]