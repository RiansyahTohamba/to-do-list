from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException

class NewVisitorTest(FunctionalTest):

	def main(self): 
		# Rian has heard about a cool new online to-do app.
		# He goes to check out its homepage
		self.browser.get(self.live_server_url)
		
		# he notices the page title and header mention to-do lists
		self.assertIn('To-Do', self.browser.title) 
		
		# he visits that URL - her to-do list is still there.
		# Satisfied, he goes back to sleep
		self.fail('Finish the test!')

		browser.quit()


	