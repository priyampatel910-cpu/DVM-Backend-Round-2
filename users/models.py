from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator


class User(AbstractUser):
    balance = models.IntegerField(MinValueValidator(0), default = 0, blank=False)

    def __str__(self):
        return f"{self.username}"

        
