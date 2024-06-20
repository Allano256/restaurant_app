from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import ReviewForm, CancelForm ,CustomerRegistrationForm
from django.views import View
from django.contrib import messages
from django.views.generic.edit import FormView
from django.views.generic import ListView
from django.views.generic.base import TemplateView  #Builds view classes that render templates.
from .models import Reservation, Cancel
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.contrib.auth import authenticate, login, logout






# Create your views here.
def starting_page(request):
    
    return render(request, "booking/index.html")


class ReserveView(LoginRequiredMixin, CreateView):
    """
    These variables help us to identify which form,template to show the user and template to return incase of successful submission.
    """
    model = Reservation
    form_class = ReviewForm
    template_name = 'booking/review.html'
    success_url = 'booking/thank_you.html'

    """
    This function will validate and save the data to the database.
    """
    def form_valid(self, form):
        booking = form.save(commit=False)
        booking.user = User.objects.get(id=self.request.user.id)
        booking.save()
       
        return super().form_valid(form)



def CancelBookingView(view):
    """
    This function will check the Customer user name provided if it matches any bookings in the,
    database and cancel, if the form is not entered well...it wont be successfull but the,
    user gets a chance to re-enter their name.
    """
    template_name = 'booking/cancel.html'
    form_class = CancelForm


    def get(self, request):
        form = self.form_class()
        print(request)
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

           
# class AsanteView(View):
    
#     def get(self, request):
#         return render(request, "booking/asante.html")
   
   
   

class Thank_youView(TemplateView):
    """
    This template will return a template indicating a summary of the Reservation.
    """
    template_name = "booking/thank_you.html"


    def get_context_data(self, **kwargs):
        """
        This method will get the details of the booking and present them to the user,
        after a succesfully submitted form
        """
        context =super().get_context_data(**kwargs)
        summary = Reservation.objects.filter(user__id=self.request.user.id)
        
        # print(len(list(summary)))

        # for i in list(summary):
        #     print(i.user.id, self.request.user.id)

        context["summary"] = summary
        return context

        

class CancelBookingView(View):
    def get(self, request):
        form = ReviewForm


def user_registration(request):
    if request.method == 'POST':
        form =CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user_name.cleaned_data.get('user_name')
            messages.success(request, f" {user_name} Your account registration is successful!")
            return redirect('login')

    else:
        form = CustomerRegistrationForm()
    return render(request,'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            massages.error(request, 'Please use a valid username or password')

    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('login')



@login_required
def home(request):
    return render(request, 'home.html')


 