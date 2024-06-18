from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from django.views import View
from django.views.generic.edit import FormView
from django.views.generic import ListView
from django.views.generic.base import TemplateView  #Builds views that render templates.
from .models import Review, Cancel




# Create your views here.
def starting_page(request):
    
    return render(request, "booking/index.html")


class ReservationView(FormView):
    """
    These variables help us to identify which form,template to show the user and template to return incase of successful submission.
    """
    form_class = ReviewForm
    template_name = 'booking/review.html'
    success_url = 'booking/thank_you.html'

    """
    This function will validate and save the data to the database.
    """
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

# class ReservationView(View):
#     """
#     This  class based view  will record reservations and save it to the database.
    
#     """
#     def get(self, request):
#         form = ReviewForm()

#         return render(request, "booking/review.html", {
#         "form": form
#     } )
    
#     def post(self, request):
#         form = ReviewForm(request.Post)
        
#         if form.is_Valid():
#             form.save()
#             return HttpResponserRedirect("booking/thank_you.html")


#         return render(request, "booking/review.html", {
#         "form": form
#     } )




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



def get_name(Review):
    """
Helper function to help us get the name of the customer to cancel their booking.
"""
    return Review['name']

def cancel_booking(request):
    """
    This is a function that cancels or deletes a reservation.
    """
    sorted_reservation = Review.sort(key=get_name)
    if sorted_reservation == user_input:
        sorted_reservation.delete()
        
    return render(request, "booking/cancel_booking")


# def thank_you(request):
#     return HttpResponse("booking/thank_you.html")

class thank_youView(TemplateView):
    """
    This view will post a confirmation message of the reservation.
    """
    template_name = "booking/thank_you.html"

    def get_context_data(self, **kwargs ):
       context =  super().get_context_data(**kwargs)
       details = Review.objects.all()
       context['message']  = "A summary of your booking"
       
       
       return context

class thank_youListView(TemplateView):
    template_name = "booking/thank_you_list.html"


    def get_context_data(self, **kwargs):
        """
        This method will get the details of the booking and present them to the user,
        after a succesfully submitted form
        """
        context =super().get_context_data(**kwargs)
        summary= Review.objects.all()
        context["summary"] = summary
        return context

        

class CancelBookingView(View):
    def get(self, request):
        form = ReviewForm




 