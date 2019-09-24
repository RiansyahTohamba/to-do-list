from selenium import webdriver
from django.test import LiveServerTestCase

class NewVisitorTest(LiveServerTestCase):
#
	def setUp(self): #
        options = Options()
        options.add_argument('--dns-prefetch-disable')
        options.add_argument('--no-sandbox')
        options.add_argument('--headless')
        options.add_argument('disable-gpu')
        try:
            self.browser = webdriver.Chrome('./chromedriver.exe',
                options=options)
        except:
            self.browser = webdriver.Chrome('./chromedriver',
                options=options)
        self.browser.implicitly_wait(3)

	def tearDown(self): #
		self.browser.quit()

	def test_homepage(self): #
		# Rian has created a homepage
		# He goes to check out its homepage
		self.browser.get(self.live_server_url)

		# He notices the page title and header mention to-do lists
		self.assertIn('Homepage', self.browser.title) #
		self.fail('Finish the test!') #
		
		# Satisfied, He goes back to sleep
		browser.quit()

if __name__ == '__main__': #
	unittest.main(warnings='ignore')
