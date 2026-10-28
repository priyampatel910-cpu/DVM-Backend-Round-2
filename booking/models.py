from django.db import models
from users.models import User
from django.utils import timezone

# Create your models here.

class Event(models.Model):
    name = models.CharField()
    category = models.CharField(null=True, blank=True, default=None)
    venue = models.CharField()
    datetime = models.DateTimeField()
    ticketprice = models.IntegerField()
    organizer = models.ForeignKey(User, default=None, on_delete=models.CASCADE, related_name="organized_events")
    available_slots = models.PositiveIntegerField(default=0)
    booked_slots = models.PositiveIntegerField(default=0)
    audience = models.ManyToManyField(User, related_name="events", blank=True)

    def __str__(self):
        return f"{self.name}, Rs. {self.ticketprice}"

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="bookings")
    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.first_name} booked {self.event.name}"

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="transaction")
    description  =  models.CharField()
    change = models.IntegerField(default=0)
    transaction_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.first_name}'s account balance change: {self.change} at {self.transaction_at}"

    @property

    def transaction_type(self):
        if self.change > 0:
            return "credit"

        else:
            return 'debit'