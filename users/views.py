from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import *

def login_view(request):
    if request.method =="POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            return render(request, 'login.html', {
                'message' : 'Invalid credential(s)'
            })

    return render(request, 'login.html')

def signup_view(request):
    if request.method == "POST":
        form = CustomAdminUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        
        else:
            return render(request, 'signup.html', {
                'message' : 'Invalid Credentials!'
            })
    return render(request, 'signup.html')

def home(request):
    if request.user.is_authenticated():
        return render(request, 'user_homepage.html')
    
    else:
        return render(request, 'homepage.html')