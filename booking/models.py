from django.db import models
from users.models import User

# Create your models here.

class Event(models.Model):
    name = models.CharField()
    venue = models.CharField()
    datetime = models.DateTimeField()
    ticketprice = models.IntegerField()
    audience = models.ManyToManyField(User, related_name="events")

    def __str__(self):
        return f"{self.name}, Rs. {self.ticketprice}"