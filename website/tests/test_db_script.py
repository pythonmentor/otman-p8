""" File testing database script """

from website.db_script import *
import requests
import json
import codecs

from django.test import TestCase

class TestDbScript(TestCase):
    """Database tests class"""
    
    def setUp(self):
        """ Create a test product """
        
        self.product = {
            "product_name" : "nutella",
            "nutrition_grade_fr" : "e",
            'nutriments' : {
                'energy_100g' : '5',
                'sugars_100g' : '5',
                'salt_100g' : '5',
                'fat_100g' : '5',
                'saturated-fat_100g' : '5',
                'sodium_100g' : '5',
                'proteins_100g' : '5',
                'carbohydrates_100g' : '5',
                },
            'categories' : 'Pâte à tartiner',
            'stores' : 'Carrefour',
            'url' : 'testurl.com',
            'image_url' : 'testimageurl.com',
            'image_small_url' : 'testimagesmallurl.com'
        } 

   
#    def test_api_request(self, monkeypatch):
#       """ Testing the OFF API request """
#       search_request = requests.get("https://fr.openfoodfacts.org/cgi/search.pl",{
#               'action': 'process',
#               'tagtype_0': 'categories', #categories selected
#               'tag_contains_0': 'contains', #contains or not
#               'sort_by': 'unique_scans_n',
#               'countries': 'France',
#               'json': 1,
#               'page': 1,
#               'page_size' : 1000
#               })
#       with codecs.open("website\tests\test_off_api_request.json","w", "utf-8-sig") as f:
#           f.write(search_request.text)
#           f.close()
#       with codecs.open("website\tests\test_off_api_request.json","r", "utf-8-sig") as f:
#           results = json.loads(f.read())
#
#       class MockRequestsGet:
#           def __init__(self, url, params=None):
#               pass
#           def json(self):
#               return results
#
#       monkeypatch.setattr('requests.get', MockRequestsGet)
#
#       self.assertEquals(api_request(1), results)

    def test_product_name(self):
        self.assertEquals(product_name(self.product), "nutella")

    def test_has_nutriscore(self):
        self.assertEquals(has_nutriscore(self.product), "e")

    def test_product_nutriments(self):
        data = {
            'energy_100g' : '5',
            'sugars_100g' : '5',
            'salt_100g' : '5',
            'fat_100g' : '5',
            'saturated-fat_100g' : '5',
            'sodium_100g' : '5',
            'proteins_100g' : '5',
            'carbohydrates_100g' : '5'
        }
        self.assertEquals(product_nutriments(self.product), data)

    def test_product_infos(self):
        data = {
            'categories' : 'Pâte à tartiner',
            'stores' : 'Carrefour',
            'url' : 'testurl.com',
            'image_url' : 'testimageurl.com',
            'image_small_url' : 'testimagesmallurl.com'
        }
        self.assertEquals(product_infos(self.product), data)