from urllib import request
from django.db import models
from django.conf import settings
from email.policy import default
from unicodedata import category
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()


class Order (models.Model):

    user = models.TextField()
    carType = models.TextField()
    fuelType = models.TextField()
    litter = models.FloatField()
    address = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    price = models.FloatField()
    payed = models.TextField()
    status = models.BooleanField()
    extraService = models.TextField()

    def __str__(self):

        return self.carType
