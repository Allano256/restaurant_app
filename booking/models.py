from django.db import models



# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=50 ,unique=True)
    email = models.EmailField(max_length=50, blank=True)
    phone = models.CharField(max_length=50)


    def __str__(self):
        return self.name
        


class Booking(models.Model):
    number_of_guests = models.IntegerField(default=0 ,unique=True)
    date = models.DateField()
    time = models.TimeField()
    message_to_restaurant = models.CharField(max_length=100, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.number_of_guests} {self.date}  {self.time} {self.message_to_restaurant}"


class CancelBooking(models.Model):
    name = models.CharField( max_length=50 ,unique=True)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, null=True)


    def __str__(self):
         return self.name


class Review(models.Model):
    name = models.CharField(max_length=50 ,unique=True)
    email = models.EmailField(max_length=50, blank=True)
    phone = models.CharField(max_length=50)
    number_of_guests = models.IntegerField(default=0 ,unique=True)
    date = models.DateField()
    time = models.TimeField()
    message_to_restaurant = models.CharField(max_length=100, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
   
   
# class Feedback(models.Model):
#     reservation = models.CharField(max_length=100)
#     time = models.TimeField()
#     date = models.DateField()
#     guest = models.IntegerField()