from django.db import models


# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=50 ,unique=True)
    email = models.EmailField(max_length=50)
    phone = models.IntegerField()
    number_of_guests = models.IntegerField(default=0 ,unique=True)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.name

