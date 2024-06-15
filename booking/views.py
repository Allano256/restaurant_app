from django.shortcuts import render
from django.http import HttpResponse
from .models import Booking, CancelBooking, Customer



# Create your views here.
def starting_page(request):
    
    return render(request, "booking/index.html")


def cancel_booking(request):
    return render(request, 'booking/cancel_booking')


def book(request):
    return render(request, 'booking/book.html')



 