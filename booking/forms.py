from django import forms

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



class ReviewForm(forms.ModelForm):
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
            'date_of_month':  DateInput(),
            'time_of_day': TimeInput(),
         }

class CancelForm(forms.Form):
    """
    This will be displayed for the user to cancel a reservation.
    """
    name_user = forms.CharField(label='Name')


class CustomerRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields =['username', 'email', 'password1', 'password2'] 
