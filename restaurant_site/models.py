from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length = 200, unique=True)
    last_name = models.CharField(max_length = 200, unique=True)
    customer_email = models.CharField(max_length = 200, unique=True)
    number_of_tables = models.IntegerField(default=0)
    number_of_guests = models.IntegerField(default=0)
    message_to_restaurant = models.TextField()
    booked_on = models.DateTimeField(auto_now_add=True)
  

