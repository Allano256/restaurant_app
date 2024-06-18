from django import forms

from .models import Reservation

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

