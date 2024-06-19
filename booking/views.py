from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import ReviewForm, CancelForm
from django.views import View
from django.contrib import messages
from django.views.generic.edit import FormView
from django.views.generic import ListView
from django.views.generic.base import TemplateView  #Builds views that render templates.
from .models import Reservation, Cancel




# Create your views here.
def starting_page(request):
    
    return render(request, "booking/index.html")


class ReserveView(FormView):
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



def CancelBookingView(view):
    """
    This function will check the Customer user name provided if it matches any bookings in the,
    database and cancel, if the form is not entered well...it wont be successfull but the,
    user gets a chance to re-enter their name.
    """
    template_name = 'cancel.html'
    form_class = CancelForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = form_class(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            reservation_id = form.cleaned_data['reservation_id']
            reservation = get_object_or_404(Reservation, id=reservation_id, name_user=name)

            if reservation.status == 'cancelled':
                messages.info(request, 'This booking is cancelled already.')

            else:
                reservation.status = 'cancelled'
                reservation.save()
                message.success(request, 'Your reservation is cancelled.')
            return redirect('booking/cancel.html')

        return render(request, self.template_name, {'form': form})

           


class thank_youListView(TemplateView):
    template_name = "booking/thank_you.html"


    def get_context_data(self, **kwargs):
        """
        This method will get the details of the booking and present them to the user,
        after a succesfully submitted form
        """
        context =super().get_context_data(**kwargs)
        summary= Reservation.objects.all()
        context["summary"] = summary
        return context

        

class CancelBookingView(View):
    def get(self, request):
        form = ReviewForm




 