

from django.db import models
from datetime import datetime
from django.contrib.auth.models import User



# Create your models here.
class Reservation(models.Model):
   
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name_user = models.CharField(max_length=50)
    email_user = models.EmailField(max_length=50, blank=True)
    phone_user = models.CharField(max_length=15 , default =None)
    number_of_guests = models.IntegerField()
    date_of_month = models.DateField(default=None)
    time_of_day = models.TimeField(default=None)
    message_to_restaurant = models.TextField(max_length=100, blank=True)
   
    
    def __self__(self):
        return self.name_user

   
   





  

