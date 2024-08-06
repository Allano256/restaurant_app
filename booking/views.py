

from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import ReserveForm, CancelForm , EditForm
from django.views import View, generic
from django.contrib import messages
from django.views.generic.edit import FormView,  UpdateView
from django.views.generic import ListView, DetailView
from .models import Reservation
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from datetime import date, datetime
from django.http import HttpResponseForbidden




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

    def form_valid(self, form):
        # Extract the cleaned data
        booked_time = form.cleaned_data['time_of_day']
        booking_date = form.cleaned_data['date_of_month']
        current_time = datetime.now().time()

        # Check if the booking date is today and the time is in the past
        if booking_date == date.today() and booked_time < current_time:
            form.add_error('time_of_day', 'The time cannot be in the past for today\'s bookings.')
            return self.form_invalid(form)

        # Associate the form instance with the user
        form.instance.user = self.request.user
        messages.success(self.request, 'Thank you for making your reservation with us, a table has been reserved for you.')
        
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('booking:single_reservation', args=[self.object.pk])



class ReserveViewList(LoginRequiredMixin,  generic.ListView):
    """
    This view will display all the bookings in the system.

    """
   
    template_name = 'reservation_list.html'

    def get_queryset(self):
        return Reservation.objects.filter(user=self.request.user)




def single_reservation(request, pk):
    """
    This  view will output a single result of the reservation made by a specific customer.
    """
   
    reservation = get_object_or_404(Reservation, pk=pk)

    if reservation.user != request.user:
        return HttpResponseForbidden("You are not allowed to access this reservation.")
        
    
    return render(request,'booking/single_reservation.html', {'reservation': reservation})
 




@login_required
def cancel_reservation(request, reservation_id ):
    """ This view will cancel a booking. 
    """

    reservation = get_object_or_404(Reservation, pk=reservation_id)

    if reservation.user != request.user:
        return HttpResponseForbiden("You are not allowed to delete this reservation.")

    if reservation.user == request.user:
        reservation.delete()
        messages.add_message(request, messages.SUCCESS, 'Reservation has been deleted successfully!')
    else:
        messages.add_message(request, messages.ERROR, 'There was an error cancelling your reservation,please check the details entered and try again. If the problem persists please contact the restaurant via telephone. ')
    return HttpResponseRedirect(reverse('booking:reserve'))


   
def update_reservation(request, reservation_id):
    change = get_object_or_404(Reservation, pk=reservation_id)
    form = EditForm(instance=change)

    if change.user != request.user:
        return HttpResponseForbiden("You are not allowed to edit this reservation.")

    if request.method == 'POST':
        form = ReserveForm(request.POST, instance= change)
        if form.is_valid() and change.user == request.user:
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Your reservation has been updated successfully!')

        else:
            messages.add_message(request, messages.ERROR, 'Error updating your reservation!')
        
        
    context = {'form': form, 'reservation': change }
    

    return render(request, 'booking/update.html', context)















  

        









 