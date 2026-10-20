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
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        
    else:
        form = CustomUserCreationForm()

    return render(request, 'signup.html', {
        'form' : form,
    })

def home(request):
    if request.user.is_authenticated:
        return render(request, 'user_homepage.html')
    
    else:
        return render(request, 'homepage.html')

def homeredirect(request):
    return redirect('home')

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)

    return redirect('home')