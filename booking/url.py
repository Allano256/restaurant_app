
from django.urls import path
from . import views

app_name = 'booking'

urlpatterns = [
    path('', views.starting_page, name='starting_page'), 
    path('reserve/', views.ReserveView.as_view(), name ='reserve'),
    # path('thanks/', views.ThankYouView.as_view(), name='thanks'),
    path('thanks', views.thanks, name='thanks'), 
    path('reserve_list', views.ReserveViewList.as_view()),
    # path('cancel/<int:pk>/', views.CancelBookingView.as_view(), name='cancel'),
    path('reservation/<int:pk>/', views.SingleReservationView.as_view),
   
]