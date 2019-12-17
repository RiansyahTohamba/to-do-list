import os
from datetime import datetime
from django.conf import settings
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
import time

from .management.commands.create_session import create_pre_authenticated_session

MAX_WAIT = 10

def wait(fn):
	def modified_fn(*args, **kwargs):
		start_time = time.time()
		while True:
			try:
				return fn(*args, **kwargs)
			except (AssertionError, WebDriverException) as e:
				if time.time() - start_time > MAX_WAIT:
					raise e
				time.sleep(0.5)
	return modified_fn

class FunctionalTest(StaticLiveServerTestCase):

	def setUp(self): #
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self): #
		self.browser.quit()
		
	def get_item_input_box(self):
		return self.browser.find_element_by_id('id_new_item')

	def add_list_item(self, item_text):
		num_rows = len(self.browser.find_elements_by_css_selector('#id_list_table tr'))
		self.get_item_input_box().send_keys(item_text)
		self.get_item_input_box().send_keys(Keys.ENTER)
		item_number = num_rows + 1
		self.wait_for_row_in_list_table(f'{item_number}: {item_text}')
		
	@wait
	def wait_for(self, fn):
		return fn()

	@wait
	def wait_for_row_in_list_table(self, row_text):
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn(row_text, [row.text for row in rows])

	@wait
	def wait_to_be_logged_in(self, email):
		self.browser.find_element_by_link_text('Log out')

	@wait
	def wait_to_be_logged_out(self, email):
		self.browser.find_element_by_name('email')
		navbar = self.browser.find_element_by_css_selector('.navbar')
		self.assertNotIn(email, navbar.text)

	def create_pre_authenticated_session(self, email):
		session_key = create_pre_authenticated_session(email)

		## to set a cookie we need to first visit the domain.
		## 404 pages load the quickest!
		self.browser.get(self.live_server_url + "/404_no_such_url/")
		self.browser.add_cookie(dict(
		    name=settings.SESSION_COOKIE_NAME,
		    value=session_key,
		    path='/',
		))

