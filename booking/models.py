from django.db import models
from datetime import datetime
# from django.contrib.auth.models import User



# Create your models here.
class Review(models.Model):
    name = models.CharField(max_length=50 ,unique=True)
    email = models.EmailField(max_length=50, blank=True)
    phone = models.CharField(max_length=50)
    number_of_guests = models.IntegerField(default=0 ,unique=True)
    date = models.DateField()
    time = models.TimeField()
    message_to_restaurant = models.CharField(max_length=100, blank=True)

   

class Cancel(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name="customer" )
    name = models.CharField(max_length=50,)

    def __str__(self):
        return f"{self.name}"

  
