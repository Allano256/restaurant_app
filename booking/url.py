from django.urls import path
from . import views

app_name = 'booking'

urlpatterns = [
    path('', views.starting_page, name='starting_page'),
    # path('reservation', views.reservation, name = 'book'),
    path('cancel',views.cancel_booking, name= 'cancel'),
    path('thanks', views.thank_you, name='thank_you'),
    path('reservation', views.ReservationView.as_view()),
  
]