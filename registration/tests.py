from django.test import TestCase
from django.urls import resolve, reverse
from . import views

# Create your tests here.

class TestUrls(TestCase):
    
    def test_list_url_is_resolved(self):
        url = reverse('signup')
        print(resolve(url))
        self.assertEqual(resolve(url).func, views.register)