from django import forms

from .models import Review

# class ReviewForm(forms.Form):
#     name = forms.CharField(max_length=50 )
#     email = forms.EmailField(max_length=50)
#     phone = forms.CharField(max_length=50)
#     number_of_guests = forms.IntegerField( )
#     date = forms.DateField()
#     time = forms.TimeField()
#     message_to_restaurant = forms.CharField(widget=forms.Textarea, max_length=200, required=False, label="Leave a message to the restaurant")
   
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
