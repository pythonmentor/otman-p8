""" File testing controller script """ 

from django.test import TestCase
from website.models import Product
from website.controller import *

class TestController(TestCase):
    """Controller tests class"""
    
    def setUp(self):
        """ Create a test product """
        
        self.test_product = Product.objects.create(
            name="nutella",
            category="Pâte a tartiner",
            nutriscore="e",
            stores="Carrefour",
            url="testurl.com",
            image_url="testimageurl.com",
            image_small_url="testimagesmallurl.com",
            energy="5",
            sugar="5",
            salt="5",
            fat="5",
            saturated_fat="5",
            sodium="5",
            proteins="5",
            carbohydrates="5"
            )
        self.test_product.save()

    def test_get_product_infos(self):
        data = { 
        'id' : 1,
        'name' : "nutella",
        'nutriscore' : "e",
        'category' : "Pâte a tartiner",
        'stores' : "Carrefour",
        'url' : "testurl.com",
        'image_url' : "testimageurl.com",
        'image_small_url' : "testimagesmallurl.com",
        'energy' : "5",
        'sugar' : "5",
        'salt' : "5",
        'fat' : "5",
        'saturated_fat' : "5",
        'sodium' : "5",
        'proteins' : "5",
        'carbohydrates' : "5",
        }
        self.assertEquals(get_product_infos(self.test_product), data)