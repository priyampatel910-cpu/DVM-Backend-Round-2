from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    balance = models.PositiveIntegerField(verbose_name="Balance", blank=False, default=0)

    def __str__(self):
        return f"{self.username}"

        
