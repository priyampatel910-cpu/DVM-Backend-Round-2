from django.shortcuts import render
from .models import Event

# Create your views here.

def events_index(request):
    events = Event.objects.all()

    return render(request, 'eventlist.html', {
        'events' : events,
    })
