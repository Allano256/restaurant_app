from django.contrib import admin
from .models import Booking, Customer, CancelBooking


# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone" ) 

class BookingAdmin(admin.ModelAdmin):
    list_display = ("number_of_guests", "date", "time" , "message_to_restaurant", "customer" ) 




admin.site.register(Customer, CustomerAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(CancelBooking)
