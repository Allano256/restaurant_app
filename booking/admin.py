from django.contrib import admin
from .models import  Review, Cancel


# Register your models here.
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("name","email","phone","number_of_guests","date","time","message_to_restaurant")

admin.site.register(Review, ReviewAdmin)
admin.site.register(Cancel)
