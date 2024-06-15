from django.urls import path
from . import views

app_name = 'booking'

urlpatterns = [
    path('', views.starting_page, name='starting_page'),
    path('book', views.book, name = 'book'),
    path('cancel',views.cancel_booking, name= 'cancel'),
]