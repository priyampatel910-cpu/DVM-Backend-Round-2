from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import *
from booking.models import *
from django.db import transaction

def login_view(request):
    if request.method =="POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('users:home')

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
            return redirect('users:home')
        
    else:
        form = CustomUserCreationForm()

    return render(request, 'signup.html', {
        'form' : form,
    })

def home(request):
    if request.user.is_authenticated:
        events = request.user.events.all()
        transactions = request.user.bookings.all()
        return render(request, 'user_homepage.html', {
            'events' : events,
            'transactions' : transactions
        })
    else:
        return render(request, 'homepage.html')

def homeredirect(request):
    return redirect('users:home')

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)

    return redirect('users:home')

def addmoney(request):
    if request.method == "POST":
        added_balance = request.POST['addeed_balance']

        with transactions.atomic():
            selected_user = User.objects.select_for_update().get(id=request.user.id)

            if added_balance<=0:
                return render(request, 'addmoney.html',{
                    'error_msg' : "Error: You must add a valid balance to proceed"
                })

            selected_user.balance += added_balance
            selected_user.save(update_fields=['balance'])

            Transaction.objects.create(user=request.user, description="Added to wallet", change=added_balance)

            return redirect('users:add_success')

    return render(request, 'addmoney.html')