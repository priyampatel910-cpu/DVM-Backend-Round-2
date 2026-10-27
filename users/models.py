from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    balance = models.PositiveIntegerField(verbose_name="Balance", blank=False, default=0)
    is_organizer = models.BooleanField(default=False, help_text="Only give this permission to oragnizer.")

    def __str__(self):
        return f"{self.username}, Organizer: {self.is_organizer}"

        
