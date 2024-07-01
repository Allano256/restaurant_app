

from django.db import models
from datetime import datetime
from django.contrib.auth.models import User




# Create your models here.
class Reservation(models.Model):
    STATUS_CHOICE = [
        ('active', 'Active'),
        ('cancelled', 'Cancelled'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name_user = models.CharField(max_length=50)
    email_user = models.EmailField(max_length=50, blank=True)
    phone_user = models.CharField(max_length=50 , default =None)
    number_of_guests = models.IntegerField(default=0,)
    date_of_month = models.DateField(default=None)
    time_of_day = models.TimeField(default=None)
    message_to_restaurant = models.CharField(max_length=100, blank=True)
    status  = models.CharField(max_length=10, choices=STATUS_CHOICE, default='active')

   
   

class Cancel(models.Model):

    review = models.ForeignKey(Reservation, on_delete=models.CASCADE, related_name="customer" )
    name = models.CharField(max_length=50,)

    def __str__(self):
        return f"{self.name}"





  

