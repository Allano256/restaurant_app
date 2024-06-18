from django.db import models
from datetime import datetime
# from django.contrib.auth.models import User



# Create your models here.
class Reservation(models.Model):
    name_user = models.CharField(max_length=50 ,unique=True, default=None)
    email_user = models.EmailField(max_length=50, blank=True)
    phone_user = models.CharField(max_length=50 , default =None)
    number_of_guests = models.IntegerField(default=0 ,unique=True)
    date_of_month = models.DateField(default=None)
    time_of_day = models.TimeField(default=None)
    message_to_restaurant = models.CharField(max_length=100, blank=True)

   

class Cancel(models.Model):
    review = models.ForeignKey(Reservation, on_delete=models.CASCADE, related_name="customer" )
    name = models.CharField(max_length=50,)

    def __str__(self):
        return f"{self.name}"

  
