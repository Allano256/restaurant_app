
from django.urls import path
from . import views

app_name = 'booking'

urlpatterns = [
    path('', views.starting_page, name='starting_page'), 
    path('reserve/', views.ReserveView.as_view(), name ='reserve'),
    # path('thanks/', views.ThankYouView.as_view(), name='thanks'),
    path('thanks', views.thanks, name='thanks'), 
    path('reserves/', views.ReserveViewList.as_view()),
    path('cancel/<int:reservation_id>/', views.cancel_reservation, name='cancel'),
    path('reserves/<int:pk>/', views.single_reservation, name='single_reservation'),
   
]