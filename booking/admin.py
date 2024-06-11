from django.contrib import admin
from .models import Booking


# Register your models here.
class BookingAdmin(admin.ModelAdmin):
    list_display = ("name","number_of_guests" )

admin.site.register(Booking, BookingAdmin)
