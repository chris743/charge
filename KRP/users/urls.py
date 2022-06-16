from django.urls import path
from . import views
from charge import views as chargeView

urlpatterns = [


    path('', chargeView.home, name="home"),

    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('denied/', views.accessDenied, name='denied')


]