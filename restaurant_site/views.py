from django.shortcuts import render
from django.views import generic
from .models import Booking
# from django.http import HttpResponse

# Create your views here.
#generic.ListView class to display all your bookings
class BookingList(generic.ListView):
    queryset = Booking.objects.all()
    template_name = "post_list.html"
    
