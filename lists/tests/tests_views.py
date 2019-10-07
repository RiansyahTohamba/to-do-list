from django.http import HttpRequest
from django.urls import resolve
from django.test import TestCase
from lists.models import Item
from lists.views import *


class HomePageTest(TestCase):
    def test_only_saves_items_when_necessary(self):
        self.client.get('/')
        self.assertEqual(Item.objects.count(), 0)

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>Homepage</title>', html)
        self.assertTrue(html.strip().endswith('</html>'))
        self.assertTemplateUsed(response, 'home.html')

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_a_POST_request(self):
        self.client.post('/', data={'item_text': 'A new list item'})
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_contains_owner_name(self):
        request = HttpRequest() #
        response = home_page(request) #
        content = response.content.strip().decode()
        self.assertIn('Muhammad Riansyah Tohamba', content)

    def test_redirects_after_POST(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/lists/the-only-list-in-the-world/')

    def test_displays_all_list_items(self):
        Item.objects.create(text='itemey 1')
        Item.objects.create(text='itemey 2')
        response = self.client.get('/')
        self.assertIn('itemey 1', response.content.decode())
        self.assertIn('itemey 2', response.content.decode())

    def test_display_vacation_comment(self):
        Item.objects.all().delete()
        response = self.client.get('/')
        self.assertIn('yey, waktunya berlibur', personal_comment(Item.objects.all()))

    def test_display_busy_comment(self):
        Item.objects.create(text='itemey 1')
        Item.objects.create(text='itemey 2')
        response = self.client.get('/')
        self.assertIn('sibuk tapi santai', personal_comment(Item.objects.all()))
        
    def test_display_oh_no_comment(self):
        tasks = ["tasks 1", "tasks 2", "tasks 3",'tasks 4','tasks 5']
        for ta in tasks:
            Item.objects.create(text=ta)

        response = self.client.get('/')
        self.assertIn('oh tidak', personal_comment(Item.objects.all()))

class ItemModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(second_saved_item.text, 'Item the second')