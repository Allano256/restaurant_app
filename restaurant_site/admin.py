from django.contrib import admin
from .models import Customer, Booking

# Register your models here.
#The admin.py file is where we register our custom models so that they can be accessed through the admin panel
admin.site.register(Customer)
admin.site.register(Booking)
