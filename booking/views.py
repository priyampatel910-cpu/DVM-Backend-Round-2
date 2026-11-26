from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.db import transaction
from django.db.models import F
from users.models import User
from django.utils import timezone

# Create your views here.

def events_index(request):
    if not request.user.is_authenticated:
        return redirect('users:login')

    events = Event.objects.filter(datetime__gt=timezone.now()).only(
        'id',
        'category',
        'name',
        'datetime',
        'venue',
        'ticketprice'
    )

    return render(request, 'eventlist.html', {
        'events' : events,
    })

def events_book(request, event_id):
    user = request.user

    if not user.is_authenticated:
        return redirect('users:login')
    
    if request.method == "POST":
        with transaction.atomic():
            event = Event.objects.filter(pk=event_id).select_related('organizer').select_for_update(of=('self', )).first()

            is_already_booked = event.audience.filter(id=user.id).exists()

            if is_already_booked:
                return render(request, 'events_book.html',{
                    'is_already_booked' : True,
                    'event' : event,
                })
            
            if event.available_slots - event.booked_slots < 1:
                return render(request, 'events_book.html', {
                    'error_message' : "Tickets are sold out!",
                    'event' : event,
                })
            
            if user.balance < event.ticketprice:
                return render(request, 'events_book.html', {
                    'insufficient_funding' : "Your wallet balance is too low for this ticket.",
                    'event' : event,
                })

            balance_updated = User.objects.filter(pk=user.pk, balance__gte=event.ticketprice).update(balance=F("balance") - event.ticketprice)

            event.booked_slots = F('booked_slots') + 1

            event.audience.add(user)
            event.save()
            
            Booking.objects.create(user=user, event=event)

            Transaction.objects.create(user=user, description=event.name, change= -event.ticketprice)

            return redirect('booking:booking_success')

    event = get_object_or_404(Event.objects.select_related("organizer"), pk = event_id)

    return render(request, 'events_book.html', {
        'event' : event
    })

def booking_success(request):
    return render(request, 'booking_success.html')