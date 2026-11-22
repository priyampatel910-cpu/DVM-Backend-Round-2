from django.contrib import admin
from .models import *

# Register your models here.

class BookingAdmin(admin.ModelAdmin):
    model = Booking
    list_display = ['user__username', 'event__name', 'booked_at']
    list_select_related = ['user', 'event']

class TransactionAdmin(admin.ModelAdmin):
    model = Transaction
    list_display = ['user__username', 'description', 'transaction_at']
    list_select_related = ['user']

class EventAdmin(admin.ModelAdmin):
    model = Event
    list_display = ['name', 'ticketprice', 'organizer__first_name', 'booked_slots']


admin.site.register(Event, EventAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(Transaction, TransactionAdmin)