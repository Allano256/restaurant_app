from django.contrib import admin
from .models import Booking, Customer, CancelBooking


# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone" )  

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Booking)
admin.site.register(CancelBooking)
