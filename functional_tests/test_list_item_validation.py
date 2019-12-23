from selenium.webdriver.common.keys import Keys
from lists.forms import DUPLICATE_ITEM_ERROR
from .base import FunctionalTest

class ItemValidationTest(FunctionalTest):
	def test_cannot_add_duplicate_item(self):
		# Edith goes to the home page and accidentally tries to submit
		# an duplicate list item.
		self.browser.get(self.live_server_url)
		self.browser.find_element_by_id('id_new_item').send_keys('Buy milk')
		self.browser.find_element_by_id('btn_submit').send_keys(Keys.ENTER)
		self.wait_for_row_in_list_table('1: Buy milk')
		self.browser.find_element_by_id('id_new_item').send_keys('Buy milk')
		self.browser.find_element_by_id('btn_submit').send_keys(Keys.ENTER)
		
		# The home page refreshes, and there is an error message saying
		# that list items cannot be duplicated
		self.wait_for(lambda: self.assertEqual(  
		    self.browser.find_element_by_css_selector('.has-error').text,
		    DUPLICATE_ITEM_ERROR
		))	