from django.test import LiveServerTestCase
from selenium import webdriver
import unittest

import sys

class FunctionalTest(LiveServerTestCase):

	def setUp(self): 
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self): 
		self.browser.quit()

	
	
if __name__ == '__main__': #
	unittest.main(warnings='ignore')


