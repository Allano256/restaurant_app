from django import forms


class ReviewForm(forms.Form):
    name = forms.CharField(max_length=50 ,unique=True)
    email = forms.EmailField(max_length=50, blank=True)
    phone = forms.CharField(max_length=50)
    number_of_guests = forms.IntegerField(default=0 ,unique=True)
    date = forms.DateField()
    time = forms.TimeField()
    message_to_restaurant = forms.CharField(widget=forms.Textarea,max_length=100, blank=True)
    