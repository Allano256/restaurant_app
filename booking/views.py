from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from django.views import View
# from .models import Booking, CancelBooking, Customer, Review



# Create your views here.
def starting_page(request):
    
    return render(request, "booking/index.html")

class ReservationView(View):
    """
    This  class based view  will record reservations and save it to the database.
    
    """
    def get(self, request):
        form = ReviewForm()

        return render(request, "booking/review.html", {
        "form": form
    } )
    
    def post(self, request):
        form = ReviewForm(request.Post)
        
        if form.is_Valid():
            form.save()
            return HttpResponserRedirect("booking/thank_you.html")


        return render(request, "booking/review.html", {
        "form": form
    } )




# def reservation(request):
#     """
#     This function will record booking an save it to the database.
    
#     """

    # if request.method == 'POST':
      
    #   form = ReviewForm(request.POST)

    #   if form.is_Valid():
    #     form.save()

        # print(form.cleaned_data)

        #If you use a Model Form you can skip this part

        # review = Review(name=form.cleaned_data['name'],
        # email=form.cleaned_data['email'],
        # phone = form.cleaned_data['phone'],
        # number_of_guests =form.cleaned_data['number_of_guests'],
        # date=form.cleaned_data['date'],
        # time =form.cleaned_data['time'],
        # message_to_restaurant= form.cleaned_data['message_to_restaurant'])
          
        # review.save()
    #     return HttpResponserRedirect("booking/thank_you.html")
    # else:
    #     form = ReviewForm()
      
    # return render(request, "booking/review.html", {
    #     "form": form
    # } )



def get_name(reservation):
    """
Helper function to help us get the name of the customer to cancel their booking.
"""
    return reservation['name']

def cancel_booking(request):
    """
    This is a function that cancels or deletes a reservation.
    """
    sorted_reservation = reservation.sort(key=get_name)
    return render(request, "booking/cancel_booking")


def thank_you(request):
    return HttpResponse("Thank you for your booking.")





 