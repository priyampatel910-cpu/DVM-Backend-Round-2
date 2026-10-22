from django.shortcuts import render, redirect, get_object_or_404
from .models import Event, Booking
from django.db import transaction

# Create your views here.

def events_index(request):
    events = Event.objects.all()
    if not request.user.is_authenticated:
        return redirect('users:login')
    return render(request, 'eventlist.html', {
        'events' : events,
    })

def events_book(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    user = request.user

    if not user.is_authenticated:
        return redirect('users:login')
    
    if request.method == "POST":
        with transaction.atomic():
            selected_event = Event.objects.select_for_update().get(id=event.id)

            is_already_booked = selected_event.audience.filter(id=user.id).exists()

            if is_already_booked:
                return render(request, 'events_book.html',{
                    'is_already_booked' : is_already_booked,
                    'event' : event
                })
            
            if selected_event.available_slots < 1:
                return render(request, 'events_book.html', {
                    'error_message' : "Tickets are sold out!",
                    'event' : event
                })
            
            if user.balance < selected_event.ticketprice:
                return render(request, 'events_book.html', {
                    'insufficient_funding' : "Your wallet balance is too low for this ticket.",
                    'event' : event
                })

            user.balance -= selected_event.ticketprice
            selected_event.available_slots -= 1
            user.save(update_fields=['balance'])

            selected_event.audience.add(user)
            selected_event.save(update_fields=['available_slots'])

            Booking.objects.create(user=user, event=event)

            return redirect('booking:booking_success')

    return render(request, 'events_book.html', {
        'event' : event
    })

def booking_success(request):
    return render(request, 'booking_success.html')