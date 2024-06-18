from django import forms

from .models import Review

class ReviewForm(forms.ModelForm):
    """
    Here we infer our Review form from the Review model.
    """
    class Meta:
        model = Review
        # fields = '__all__'
        exclude = ['customer']
        labels = {
            "name":"Your name",
            "email":"Your email",
            "phone":"Your phone",
            "number_of_guests":"number of guests",
            "date":"Date",
            "time":"Time",
            "message_to_restaurant":"Leave a message to the restaurant"

        }

