from django.test import LiveServerTestCase
from selenium import webdriver
import unittest

import sys

class FunctionalTest(LiveServerTestCase):

	def setUp(self): 
		options = Options()
		options.add_argument('--headless')
		self.browser = webdriver.Firefox(options=options)
		self.browser.implicitly_wait(3)

	def tearDown(self): 
		self.browser.quit()

	
	
if __name__ == '__main__': #
	unittest.main(warnings='ignore')


