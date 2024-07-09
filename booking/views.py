

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import ReserveForm, CancelForm 
from django.views import View, generic
from django.contrib import messages
from django.views.generic.edit import FormView
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView  #Builds view classes that render templates.
from .models import Reservation, Cancel
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy




# Create your views here.
def starting_page(request):
    
    return render(request, "booking/index.html")


class ReserveView(LoginRequiredMixin, CreateView):
    """
   This class will save the data entered by the user after submission and redirect to success url!
    """
    model = Reservation
    form_class = ReserveForm
    template_name = 'booking/reserve.html'
    success_url = reverse_lazy('booking:thanks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Thank you for making your reservation with us, a table has been reserved for you.')
        return super().form_valid(form)

class ReserveViewList(LoginRequiredMixin,  generic.ListView):
    """
    This view will display all the bookings in the system.

    """
   
    template_name = 'reservation_list.html'

    def get_queryset(self):
        return Reservation.objects.all()

        # user = self.request.user
        # return Reservation.objects.filter(user=user), to get only one reservation by a user


def single_reservation(request, pk):
    """
    This  view will output a single result of the reservation made by a specific customer.
    """
   
    order = get_object_or_404(Reservation, pk=pk)


    return render(request,'booking/single_reservation.html', {'order': order})
 

def thanks(request):
    return render(request, 'booking/thank_you.html')



@login_required
def cancel_booking(request, pk ):
    """ This view will cancel a booking. """
    reservation = get_object_or_404(Reservation, pk=pk)

    if reservation.user == request.user:
        reservation.delete()
        messages.add_message(request, messages.SUCCESS, 'Reservation has been deleted successfully!')
    else:
        messages.add_message(request, messages.ERROR, 'There was an error canceling your reservation,please check the details entered and try again. If the problem persists please contact the restaurant via telephone. ')
    return HttpResponseRedirect('booking/single_reservation.html')
   






    # booking_instance = get_object_or_404(Reservation, id=reservation_id, user=request.user)

    # if request.method == 'POST':
    #     booking_instance.delete()
    #     messages.success(request, 'Reservation cancelled successfully.')
    #     return redirect('booking')

    # return render(request, 'cancel.html', {'booking_instance': booking_instance})
  




# class CancelBookingView(LoginRequiredMixin, CreateView):
#     """
#     This class will delete the identified reservation with the primary key stated in the url patterns.
#     """
#     model = Reservation
#     template_name = 'booking/cancel.html'
#     form_class = CancelForm
#     success_url = reverse_lazy('booking:reserve')


#     def reverse_view(request, pk):
#          cancel_url = reverse('cancel', args=[pk])
#          return redirect(cancel_url)





  # def get_context_data(self, **kwargs):
        
    #     context = super().get_context_data(**kwargs)
    #     review = Reservation.objects.filter(user=self.request.user)
        
    #     context["review"] = review
    #     return context



    




  

        






#     def get_context_data(self, **kwargs):
#         """
#         This method will get the details of all the bookings. 
       
#         """
#         context =super().get_context_data(**kwargs)
#         summary = Reservation.objects.all()
        
    
#         context["summary"] = summary
#         return context
#         return redirect(request,'booking/index.html' )


    




 