from datetime import datetime, date
from django import forms
from django.core.exceptions import ValidationError
from .models import Reservation
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User


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

        phone_user = forms.RegexField(
        regex=r'^\+?1?\d{9,15}$', 
        error_messages={
            'invalid': 'Enter a valid phone number. This value may contain only numbers, and should be between 9 and 15 digits long.'
        },
        max_length=15
        )

    
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
            'number_of_guests': forms.NumberInput(attrs={'min': '1', 'max':'10'}),
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
            if not( 1 <= guests_allowed <= 10) :
                raise forms.ValidationError('Number of guests can be between 1 and 10 only!')
          
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
                if not ( 1 <= guests_allowed <= 10) :
                    raise forms.ValidationError('Number of guests can only be between 1 and 10 only!')
                


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