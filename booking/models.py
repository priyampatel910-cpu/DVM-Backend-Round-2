from django.db import models
from users.models import User

# Create your models here.

class Event(models.Model):
    name = models.CharField()
    category = models.CharField(null=True, blank=True, default=None)
    venue = models.CharField()
    datetime = models.DateTimeField()
    ticketprice = models.IntegerField()
    organizer = models.CharField(null=True, default=None)
    available_slots = models.PositiveIntegerField(default=0)
    audience = models.ManyToManyField(User, related_name="events", blank=True)

    def __str__(self):
        return f"{self.name}, Rs. {self.ticketprice}"