from selenium import webdriver
from django.test import LiveServerTestCase
from selenium.webdriver.common.keys import Keys
import time


class NewVisitorTest(LiveServerTestCase):
#
	def setUp(self): #
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self): #
		self.browser.quit()

	def create_new_item(self, new_item):
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys(new_item)
		inputbox.send_keys(Keys.ENTER)
		time.sleep(2)

	def check_comment(self, comment):
		actual_comment = self.browser.find_element_by_id('personal_comment').text
		self.assertIn(comment, actual_comment)


	def check_for_row_in_list_table(self, row_text):
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn(row_text, [row.text for row in rows])

	def test_homepage(self): #
		# Rian has created a homepage
		# He goes to check out its homepage
		self.browser.get(self.live_server_url)

		# He notices the page title and header mention to-do lists
		self.assertIn('Homepage', self.browser.title) #
		
		my_name = self.browser.find_element_by_tag_name('h1').text

		self.assertIn('Muhammad Riansyah Tohamba', my_name)

		header_text = self.browser.find_element_by_tag_name('h2').text

		self.assertIn('To-Do', header_text)

		# There is still a text box inviting her to add another item. She
		# enters "Use peacock feathers to make a fly" (Edith is very
		# methodical)
		self.check_comment('yey, waktunya berlibur')
		self.create_new_item('Buy peacock feathers')
		self.check_comment('sibuk tapi santai')
		self.create_new_item('Use peacock feathers to make a fly')
		self.create_new_item('Use peacock feathers to make a fly')
		self.create_new_item('Use peacock feathers to make a fly')
		self.create_new_item('Use peacock feathers to make a fly')
		self.check_comment('oh tidak')


		# The page updates again, and now shows both items on her list
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.check_for_row_in_list_table('1: Buy peacock feathers')
		self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')
		
		# Satisfied, He goes back to sleep
		self.browser.quit()

if __name__ == '__main__': #
	unittest.main(warnings='ignore')
