
from django import forms

from .models import Reservation
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from datetime import date



class DateInput(forms.DateInput):
    """
    This class will create a date picker.
    """
    input_type = 'date'


class TimeInput(forms.DateInput):
    """
    This class will create a time picker.
    """
    input_type = 'time'



class ReserveForm(forms.ModelForm):
    """
    Here we infer our Review form from the Reservation model.
    """
    class Meta:
        model = Reservation
        # fields = '__all__'
        exclude = ['user', 'status']
        labels = {
            "name_user":"Name",
            "email_user":"Email",
            "phone_user":"Phone Number",
            "number_of_guests":"Number of Guests",
            "date_of_month":"Date",
            "time_of_day":"Time",
            "message_to_restaurant":"Leave a message to the restaurant"

        }

        widgets = {
            'date_of_month':  forms.DateInput(attrs={'type': 'date','min': date.today().isoformat()}),
            'time_of_day': TimeInput(),
         }

        def actual_date(self):
            reservation_date=self.cleaned_data['date_of_month']
            today = date.today()

            if reservation_date < now:
                raise forms.ValidationError('You cannot book a date in the past')

            return reservation_date





class CancelForm(forms.ModelForm):
    """
    This will be displayed for the user to cancel a reservation.
    """
    class Meta:
        model = Reservation
        fields = ['name_user' ]
        labels = {
            'name_user': 'Name',
            
        }

     
    

class EditForm(forms.ModelForm):
    """
    Here we infer our Review form from the Reservation model.
    """
    class Meta:
        model = Reservation
        # fields = '__all__'
        exclude = ['user', 'status']
        labels = {
            "name_user":"Name",
            "email_user":"Email",
            "phone_user":"Phone Number",
            "number_of_guests":"Number of Guests",
            "date_of_month":"Date",
            "time_of_day":"Time",
            "message_to_restaurant":"Leave a message to the restaurant"

        }

        def actual_date(self):
            reservation_date=self.cleaned_data['date_of_month']
            today = date.today()

            if reservation_date < now:
                raise forms.ValidationError('You cannot book a date in the past')

            return reservation_date
          



        time_of_day = forms.TimeField(
        widget=forms.TimeInput(attrs={'type': 'datetime-local', }),
        input_formats=['%Y-%m-%dT%H:%M'])

   

        widgets = {
            'date_of_month':  forms.DateInput(attrs={'type': 'date','min': date.today().isoformat()}),
            
         }
