from selenium import webdriver
from django.test import LiveServerTestCase

class NewVisitorTest(LiveServerTestCase):
#
	def setUp(self): #
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self): #
		self.browser.quit()

	def test_homepage(self): #
		# Rian has created a homepage
		# He goes to check out its homepage
		self.browser.get(self.live_server_url)

		# He notices the page title and header mention to-do lists
		self.assertIn('Homepage', self.browser.title) #
		
		# Satisfied, He goes back to sleep
		self.browser.quit()

if __name__ == '__main__': #
	unittest.main(warnings='ignore')
