
from django.urls import path
from . import views

app_name = 'booking'

urlpatterns = [
    path('', views.starting_page, name='starting_page'),
    path('reserve', views.ReserveView.as_view(), name ='booking'),
    path('cancel', views.CancelBookingView.as_view(), name='cancel_booking'),
    path('summary', views.Thank_youView.as_view(), name='summary_of_booking'),
    path('register', views.user_registration, name='register'),
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
 
]