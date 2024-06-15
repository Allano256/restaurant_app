from django.shortcuts import render
from django.http import HttpResponse
from .models import Booking, CancelBooking, Customer



# Create your views here.
def starting_page(request):
    
    return render(request, "booking/index.html")


def reservation(request):
    return render(request, "booking/book.html")


def cancel_booking(request):
    return render(request, "booking/cancel_booking")





 