
from django.urls import path
from . import views

app_name = 'booking'

urlpatterns = [
    path('', views.starting_page, name='starting_page'), 
    path('reserve/', views.ReserveView.as_view(), name ='reserve'),
    path('reservations/', views.ReserveViewList.as_view() , name='reservations'),
    path('cancel/<int:reservation_id>/', views.cancel_reservation, name='cancel'),
    path('reserves/<int:pk>/', views.single_reservation, name='single_reservation'),
    path('update/<int:reservation_id>', views.update_reservation, name='update'),
   
]