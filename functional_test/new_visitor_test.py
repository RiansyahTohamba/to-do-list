from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException

class NewVisitorTest(FunctionalTest):

	def main(self): 
		# Rian has created his cool homepage.
		# He goes to check out its homepage
		self.browser.get(self.live_server_url)
		
		# he notices the page title and header mention homepage lists
		self.assertIn('homepage', self.browser.title) 
		
		# Satisfied, he goes back to sleep
		self.fail('Finish the test!')

		browser.quit()


	