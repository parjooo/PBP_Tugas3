from django.test import TestCase, Client
from django.urls import resolve

# Create your tests here.
class TestCaseRespon(TestCase):
    def test_contoh_watchlist_url_exists(self):
        respon = Client().get("http://localhost:8000/mywatchlist/", follow=True)
        self.assertEqual(respon.status_code,200)
    
    def test_contoh_watchlist_html_url_exists(self):
        respon = Client().get("http://localhost:8000/mywatchlist/html/", follow=True)
        self.assertEqual(respon.status_code,200)

    def test_contoh_watchlist_json_url_exists(self):
        respon = Client().get("http://localhost:8000/mywatchlist/json/", follow=True)
        self.assertEqual(respon.status_code,200)

    def test_contoh_watchlist_xml_url_exists(self):
        respon = Client().get("http://localhost:8000/mywatchlist/xml/", follow=True)
        self.assertEqual(respon.status_code,200)
