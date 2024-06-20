
from django.urls import path
from . import views

app_name = 'booking'

urlpatterns = [
    path('', views.starting_page, name='starting_page'),
    path('reserve', views.ReserveView.as_view()),
    path('summary', views.thank_youListView.as_view()),
    path('cancel', views.CancelBookingView.as_view(), name='cancel_booking'),
    
   
]