
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

class NumberInput(forms.NumberInput):
    """
    Create a number picker
    """
    input_type = 'number'





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
            'number_of_guests': forms.NumberInput(attrs={'min': '1'}),
            'phone_user': forms.TextInput(attrs={'pattern': '[0-9]+', 'title': 'Enter numbers only' }),
           
         }

        def actual_date(self):
            reservation_date=self.cleaned_data['date_of_month']
            today = date.today()

            if reservation_date < now:
                raise forms.ValidationError('You cannot book a date in the past')

            return reservation_date

        def number_guests(self):
            guests_allowed =self.cleaned_data['number_of_guests']
            if guests_allowed <= 0:
                raise forms.ValidationError('Please enter numbers from 1 upwards!')
          
            return guests_allowed 

        def phone_number_allowed(self):
            numbers_allowed = self.cleaned_data['phone_user']
         
            if not re.match(r'^\d+$', numbers_allowed):
                raise ValidationError('Please use only numbers')

            return numbers_allowed

        





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

        def number_guests(self):
            guests_allowed =self.cleaned_data['number_of_guests']
            if guests_allowed < 0:
                raise forms.ValidationError('Please enter numbers from 1 upwards!')
          
            return guests_allowed 

       

        def phone_number_allowed(self):
            numbers_allowed = self.cleaned_data['phone_user']
         
            if not re.match(r'^\d+$', numbers_allowed):
                raise ValidationError('Please use only numbers')

            return numbers_allowed

      

        time_of_day = forms.TimeField(
        widget=forms.TimeInput(attrs={'type': 'datetime-local', }),
        input_formats=['%Y-%m-%dT%H:%M'])

   

        widgets = {
            'date_of_month': forms.DateInput(attrs={'type': 'date','min': date.today().isoformat()}),
            'number_of_guests': forms.NumberInput(attrs={'min': '1'}),
            'phone_user': forms.TextInput(attrs={'pattern': '[0-9]+', 'title': 'Enter numbers only' }),
         }
