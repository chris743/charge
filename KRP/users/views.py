from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile

# Create your views here.
def profiles(request):
    return render(request, 'users/profiles.html')

def loginPage(request):

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            print("email is not in the system")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            print("authenticated")
            return redirect('home')
        else:
            print('Username or Password was incorrect')


    return render(request, 'users/login_register.html')

def logoutUser(request):
    logout(request)
    return redirect('login')

def accessDenied(request):
    return render(request, 'users/access_Denied.html')