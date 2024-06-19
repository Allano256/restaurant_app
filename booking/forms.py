from django import forms
# from django_flatpickr.widgets import DatePickerInput, TimePickerInput
from .models import Reservation



class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.DateInput):
    input_type = 'time'



class ReviewForm(forms.ModelForm):
    """
    Here we infer our Review form from the Review model.
    """
    class Meta:
        model = Reservation
        # fields = '__all__'
        exclude = ['customer']
        labels = {
            "name_user":"Your name",
            "email_user":"Your email",
            "phone_user":"Your phone",
            "number_of_guests":"number of guests",
            "date_of_month":"Date",
            "time_of_day":"Time",
            "message_to_restaurant":"Leave a message to the restaurant"

        }
        widgets = {
            'date_of_month':  DateInput(),
            'time_of_day': TimeInput(),
         }
