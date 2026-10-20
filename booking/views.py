from django.shortcuts import render
from .models import Event

# Create your views here.

def events_index(request):
    events = Event.objects.all()
    if not request.user.is_authenticated:
        return redirect('users:login')
    return render(request, 'eventlist.html', {
        'events' : events,
    })
