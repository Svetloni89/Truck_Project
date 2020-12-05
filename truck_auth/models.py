from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from truck_auth.validators import validator_phone_only_numeric


class UserProfile(models.Model):
    phone_number = models.CharField(max_length=13, blank=True, validators=(validator_phone_only_numeric,))
    city = models.CharField(max_length=10, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}'
