from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from .models import Booking, CancelBooking, Customer



# Create your views here.
def starting_page(request):
    
    return render(request, "booking/index.html")


def reservation(request):
    if request.method == 'POST':
      form = ReviewForm(request.POST)
      if form.is_Valid():
        print(form.cleaned_data)
        return HttpResponserRedirect("booking/thank_you.html")
    else:
        form = ReviewForm()
      
    return render(request, "booking/book.html", {
        "form": form
    } )


def get_name(reservation):
    return reservation['name']

def cancel_booking(request):
    sorted_reservation = reservation.sort(key=get_name)
    return render(request, "booking/cancel_booking")


def thank_you(request):
    return HttpResponse("Thank you for your booking.")





 