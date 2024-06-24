
from django.urls import path
from . import views

app_name = 'booking'

urlpatterns = [
    path('', views.starting_page, name='starting_page'),
    path('reserve/<int:pk>/', views.ReserveView.as_view(), name ='booking'),
    path('reserve_list', views.ReserveView_List.as_view()),
    path('cancel/<int:pk>/', views.CancelBookingView.as_view(), name='cancel_booking'),
    path('summary', views.Thank_youView.as_view(), name='summary_of_booking'),
    path('reservation/<int:pk>/', views.SingleReservationView.as_view),
   
]