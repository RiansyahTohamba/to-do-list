from django.http import HttpRequest
from django.urls import resolve
from django.test import TestCase,Client
from lists.views import home_page


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve("/")
        self.assertEqual(found.func, home_page)


    def test_home_page_returns_correct_title(self):
        request = HttpRequest()
        response = home_page(request)
        content = response.content.strip()
        self.assertTrue(content.startswith(b'<html>'))
        self.assertIn(b'<title>Home</title>', response.content)
        self.assertTrue(content.endswith(b'</html>'))
