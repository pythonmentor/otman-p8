from django.test import TestCase, Client
from django.urls import reverse
from website.models import Product, User


"""File containing views tests"""

class TestViews(TestCase):
    """Views tests class"""
    
    @classmethod
    def setUpClass(cls):
        """ Create a test user and product """
        super().setUpClass()
        test_user = User.objects.create_user(email='testuser', password='password')
        test_user.save()
        test_product = Product.objects.create(
            name="nutella",
            category="Pâte a tartiner",
            nutriscore="e",
            url="testurl.com",
            image_url="testimageurl.com",
            image_small_url="testimagesmallurl.com",
            energy="400",
            sugar="6",
            salt="0",
            fat="10",
            saturated_fat="8",
            sodium="5",
            proteins="3",
            carbohydrates="4"
            )
        test_product.save()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()


    def test_index(self):
        """Test homepage view"""
        client = Client()
        response = client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'website/index.html')

    def test_redirection(self):
        """Test redirection view"""
        client = Client()
        response = client.get(reverse('redirection'))
        self.assertEquals(response.status_code, 302)

    def test_signup(self):
        """Test signup view"""
        client = Client()
        response = client.get(reverse('signup'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'website/signup.html')
    
    def test_account_redirection(self):
        """Test account redirection view"""
        client = Client()
        response = client.get(reverse('account'))
        self.assertEquals(response.status_code, 302)
    
    def test_account(self):
        """Test account view"""
        client = Client()
        client.login(email='testuser', password='password')
        response = client.get(reverse('account'))
        self.assertEqual(str(response.context['user']), 'testuser')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'website/account.html')

    def test_result(self):
        """Test result view"""
        client = Client()
        response = client.get('/result', {'search' : 'nutella'})
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'website/result.html')

    def test_product(self):
        """Test product view"""
        client = Client()
        response = client.get('/product/2')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'website/product.html')

    def test_favorites_redirection(self):
        """Test favorites redirection view"""
        client = Client()
        response = client.get(reverse('favorites'))
        self.assertEquals(response.status_code, 302)

    def test_favorites(self):
        """Test favorites view"""
        client = Client()
        client.login(email='testuser', password='password')
        response = client.get(reverse('favorites'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'website/favorites.html')

    def test_save(self):
        """Test save view"""
        client = Client()
        client.login(email='testuser', password='password')
        response = client.get('/save/2')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'website/favorites.html')

    def test_remove(self):
        """Test remove view"""
        client = Client()
        client.login(email='testuser', password='password')
        response = client.get('/remove/2')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'website/favorites.html')

    def test_contact(self):
        """Test contact view"""
        client = Client()
        response = client.get(reverse('contact'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'website/contact.html')

    def test_legal_terms(self):
        """Test legal terms view"""
        client = Client()
        response = client.get(reverse('legal_terms'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'website/legal_terms.html')