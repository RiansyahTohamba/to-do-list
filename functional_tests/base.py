from selenium import webdriver
import unittest

class FunctionalTest(unittest.TestCase):

	def setUp(self): 
		self.browser = webdriver.Firefox(options=options)
		self.browser.implicitly_wait(3)

	def tearDown(self): 
		self.browser.quit()

	
	
if __name__ == '__main__': #
	unittest.main(warnings='ignore')


