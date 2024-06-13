from django.db import models


# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=50 ,unique=True)
    email = models.EmailField(max_length=50, blank=True)
    phone = models.CharField(max_length=50)


    def __str__(self):
        return self.name
        


class Booking(models.Model):
    number_of_guests = models.IntegerField(Customer, default=0 ,unique=True)
    date = models.DateField()
    time = models.TimeField()
    message_to_restaurant = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.number_of_guests} {self.date}  {self.time} {self.message_to_restaurant}"


class CancelBooking(models.Model):
    name = models.CharField(Booking, max_length=50 ,unique=True)


    def __str__(self):
         return self.name
       




   
