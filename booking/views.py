from django.shortcuts import render
from django.http import HttpResponse
from .models import Booking



# Create your views here.
def book_table(request):
    while (True):
        table_request = input("Reservation y/n ?")
        number_people = int(input("How many people are you reserving for?"))
        response = table_request.capitalize()



   
    return render(request, "booking/booking.html")



 