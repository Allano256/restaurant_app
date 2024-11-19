from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from datetime import datetime, timedelta, date
from .forms import ReserveForm
from .models import Reservation


class TestReservationView(TestCase):
     #Create test user
    def setUp(self):
    
        # Create a test user
        self.user = User.objects.create_user(username='Mike', password='testpassword123')
        self.login_url = reverse('account_login')  
        self.reserve_url = reverse('booking:reserve') 
       

    
    def test_reservation_success(self):
        # Log in the user
        self.client.login(username='Mike', password='testpassword123')

        # Valid reservation data
        future_time = (datetime.now() + timedelta(hours=1)).time()
        valid_data = {
            'name_user': 'Mike',
            'email_user': 'mike@example.com',
            'phone_user': '+1234567890',
            'number_of_guests': 2,
            'date_of_month': date.today().isoformat(),
            'time_of_day': future_time.strftime('%H:%M'),
            'message_to_restaurant': 'Looking forward to the reservation!',
        }

        # Post the data to the reserve view
        response = self.client.post(self.reserve_url, data=valid_data)

        # Check for redirection to the success URL
        self.assertEqual(response.status_code, 302)
        reservation = Reservation.objects.get(user=self.user)
        self.assertEqual(reservation.name_user, 'Mike')
        self.assertEqual(reservation.number_of_guests, 2)

    def test_reservation_time_in_past(self):
        # Log in the user
        self.client.login(username='Mike', password='testpassword123')

        # Prepare invalid reservation data (time in the past)
        past_time = (datetime.now() - timedelta(hours=1)).time()
        invalid_data = {
            'name_user': 'Mike',
            'email_user': 'mike@example.com',
            'phone_user': '+1234567890',
            'number_of_guests': 2,
            'date_of_month': date.today().isoformat(),
            'time_of_day': past_time.strftime('%H:%M'),
            'message_to_restaurant': 'Looking forward to the reservation!',
        }

        # Post the data to the reserve view
        response = self.client.post(self.reserve_url, data=invalid_data)

        # Ensure the form is not valid and the response contains the error message
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', 'time_of_day', 'The time cannot be in the past for today\'s bookings.')

    def test_reservation_unauthenticated_user(self):
        # Attempt to access the reserve view without logging in
        response = self.client.get(self.reserve_url)

        # Check for redirection to the login page
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f'{self.login_url}?next={self.reserve_url}')