from django.contrib.auth.models import User
from django.db import models
from truck_app.validators import validator_comment_end, validator_price_is_digit


# Create your models here.
class Truck(models.Model):
    nickname = models.CharField(max_length=20)
    make = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    description = models.TextField(max_length=400)
    image = models.ImageField(upload_to='public/images')
    price = models.CharField(max_length=10, validators=(validator_price_is_digit,))
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nickname}'


class Comment(models.Model):
    truck = models.ForeignKey(Truck, on_delete=models.CASCADE)
    text = models.CharField(blank=False, max_length=100, validators=(validator_comment_end,))
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.truck}'


class Like(models.Model):
    truck = models.ForeignKey(Truck, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.truck}'
