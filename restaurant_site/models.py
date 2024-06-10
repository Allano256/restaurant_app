from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#In these two models ive created,i have linked the booking tpo a customer in that if the booking is deleted even the customer disappears,
# inotherwards this is hyow these two tables are related, the customer and the booking.
class Customer(models.Model):
    first_name = models.CharField(max_length = 200, unique=True)
    last_name = models.CharField(max_length = 200, unique=True, blank=True)
    customer_email = models.EmailField(max_length = 200, unique=True)

      
  

class Booking(models.Model):
    customer_type = models.ForeignKey( User, on_delete=models.CASCADE, related_name ="restaurant_booking"
    )
    number_of_tables = models.IntegerField(default=0,  unique=True)
    number_of_guests = models.IntegerField(default=0 ,unique=True)
    message_to_restaurant = models.TextField(blank=True)
    booked_on = models.DateTimeField(auto_now_add=True)
    # #Here i have connected the BOOKINGS TO CUSTOMER model with this code
    booking_relationship_to_Customer = models.ForeignKey(Customer, on_delete = models.CASCADE, related_name ="customer_booking")

    class Meta:
          ordering = ["-booked_on"]
  





 


