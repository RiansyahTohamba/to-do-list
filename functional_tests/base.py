import os
from datetime import datetime
from django.conf import settings
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
import time

MAX_WAIT = 10

class FunctionalTest(LiveServerTestCase):

	def setUp(self): #
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self): #
		self.browser.quit()
		
	def get_item_input_box(self):
		return self.browser.find_element_by_id('id_new_item')

	def wait_for_row_in_list_table(self, row_text):
		start_time = time.time()
		while True:  
			try:
				table = self.browser.find_element_by_id('id_list_table')  
				rows = table.find_elements_by_tag_name('tr')
				self.assertIn(row_text, [row.text for row in rows])
				return  
			except (AssertionError, WebDriverException) as e:  
				if time.time() - start_time > MAX_WAIT:  
					raise e  
				time.sleep(0.5) 
