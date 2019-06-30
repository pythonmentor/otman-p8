from django.test import TestCase
from website.forms import SignUpForm

"""File containing forms tests"""

class TestForms(TestCase):
    """Forms tests class"""

    def test_signup_form_valid(self):
        """Signup valid test"""
        form = SignUpForm(data={
            'first_name': 'first_name',
            'last_name': 'last_name',
            'email': 'test_email@test.com',
            'password1': 'ldoehs154',
            'password2': 'ldoehs154',
        })
        self.assertTrue(form.is_valid())

    def test_signup_form_invalid(self):
        """Signup invalid test"""
        form = SignUpForm(data={})
        self.assertFalse(form.is_valid())