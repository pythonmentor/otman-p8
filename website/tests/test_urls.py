from django.test import SimpleTestCase
from django.urls import resolve, reverse
from website.views import *

"""File containing url tests"""

class TestUrls(SimpleTestCase):
    """Urls tests class"""

    def test_index_url(self):
        """Test the index url"""
        url = reverse('index')
        self.assertEquals(resolve(url).func, index)

    def test_signup_url(self):
        """Test the signup url"""
        url = reverse('signup')
        self.assertEquals(resolve(url).func, signup)

    def test_account_url(self):
        """Test the account url"""
        url = reverse('account')
        self.assertEquals(resolve(url).func, account)

    def test_result_url(self):
        """Test the result url"""
        url = reverse('result')
        self.assertEquals(resolve(url).func, result)

    def test_product_url(self):
        """Test the product url"""
        url = reverse('product', args=["1"])
        self.assertEquals(resolve(url).func, product)

    def test_favorites_url(self):
        """Test the favorites url"""
        url = reverse('favorites')
        self.assertEquals(resolve(url).func, favorites)

    def test_save_url(self):
        """Test the save url"""
        url = reverse('save', args=["1"])
        self.assertEquals(resolve(url).func, save)

    def test_remove_url(self):
        """Test the remove url"""
        url = reverse('remove', args=["1"])
        self.assertEquals(resolve(url).func, remove)

    def test_contact_url(self):
        """Test the contact url"""
        url = reverse('contact')
        self.assertEquals(resolve(url).func, contact)

    def test_legal_terms_url(self):
        """Test the legal_terms url"""
        url = reverse('legal_terms')
        self.assertEquals(resolve(url).func, legal_terms)