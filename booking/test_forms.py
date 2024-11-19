from django.test import TestCase
from .forms import ReserveForm, EditForm
from datetime import date


class TestReserveForm(TestCase):
    """
    Test for all fields.
    """

    def test_form_is_valid(self):
        valid_data = {
            'name_user': 'Allan',
            'email_user': 'allan@yahoo.com',
            'phone_user': '+1234567890',
            'number_of_guests': 4,
            'date_of_month': date.today().isoformat(),
            'time_of_day': '18:30',
            'message_to_restaurant': 'Looking forward to visiting!',
        }
        reserve_form = ReserveForm(valid_data)
        self.assertTrue(reserve_form.is_valid(), msg='Reservation form is not valid')


class TestReserveForm(TestCase):
    """
    Test for all fields giving an empty email_user,name_user field.
    """
    
    def test_form_is_invalid(self):
        invalid_data = {
            'name_user': '',
            'email_user': '',
            'phone_user': '+1234567890',
            'number_of_guests': 4,
            'date_of_month': date.today().isoformat(),
            'time_of_day': '18:30',
            'message_to_restaurant': 'Looking forward to visiting!',
        }
        reserve_form= ReserveForm(invalid_data)
        self.assertFalse(reserve_form.is_valid(), msg='Reservation form is  valid')


class TestEditForm(TestCase):
    """
    Test for all fields.
    """

    def test_edit_reserve_form_is_valid(self):
        valid_data = {
            'name_user': 'Allan',
            'email_user': 'allan@yahoo.com',
            'phone_user': '+1234567890',
            'number_of_guests': 4,
            'date_of_month': date.today().isoformat(),
            'time_of_day': '18:30',
            'message_to_restaurant': 'Looking forward to visiting!',
        }
        editreserve_form = EditForm(valid_data)
        self.assertTrue(editreserve_form.is_valid(), msg='Edit form is not valid')


class TestEditForm(TestCase):
    """
    Test for all fields,giving an empty name field.
    """

    def test_edit_reserve_form_is_invalid(self):
        invalid_data = {
            'name_user': '',
            'email_user': 'allan@yahoo.com',
            'phone_user': '+1234567890',
            'number_of_guests': 4,
            'date_of_month': date.today().isoformat(),
            'time_of_day': '18:30',
            'message_to_restaurant': 'Looking forward to visiting!',
        }
        editreserve_form = EditForm(invalid_data)
        self.assertFalse(editreserve_form.is_valid(), msg='Edit form is  valid')




    