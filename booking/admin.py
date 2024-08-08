from django.contrib import admin
from .models import  Reservation


# Register your models here.
class ReservationAdmin(admin.ModelAdmin):
    list_display = ("name_user","email_user","phone_user","number_of_guests","date_of_month","time_of_day","message_to_restaurant")

admin.site.register(Reservation, ReservationAdmin)

<<<<<<< HEAD

=======
>>>>>>> f155bbe1073bad43e0b1be785af48feb5f80b4b0
