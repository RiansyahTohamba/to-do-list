from selenium import webdriver
from django.test import LiveServerTestCase
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
import time

MAX_WAIT = 10


class NewVisitorTest(LiveServerTestCase):
#
	def setUp(self): #
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self): #
		self.browser.quit()

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

	def get_item_input_box(self):
		return self.browser.find_element_by_id('id_new_item')

	def add_list_item(self, item_text):
		num_rows = len(self.browser.find_elements_by_css_selector('#id_list_table tr'))
		self.get_item_input_box().send_keys(item_text)
		self.get_item_input_box().send_keys(Keys.ENTER)
		item_number = num_rows + 1
		self.wait_for_row_in_list_table(f'{item_number}: {item_text}')

	def check_comment(self, comment):
		actual_comment = self.browser.find_element_by_id('personal_comment').text
		self.assertIn(comment, actual_comment)

	def test_can_start_a_list_for_one_user(self):
		# Rian has created a homepage
		# He goes to check out its homepage
		self.browser.get(self.live_server_url)

		# He notices the page title and header mention to-do lists
		self.assertIn('Homepage', self.browser.title) #
		
		my_name = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Muhammad Riansyah Tohamba', my_name)


		header_text = self.browser.find_element_by_tag_name('h2').text
		self.assertIn('To-Do', header_text)
		
		# no assignments at all, thereore show vacation comment
		self.check_comment('yey, waktunya berlibur')
		inputbox = self.get_item_input_box()
		# She types "Buy peacock feathers" into a text box (Edith's hobby
		# is tying fly-fishing lures)
		# When she hits enter, the page updates, and now the page lists
		# "1: Buy peacock feathers" as an item in a to-do list table
		inputbox.send_keys('Buy peacock feathers')
		inputbox.send_keys(Keys.ENTER)
		
		self.wait_for_row_in_list_table('1: Buy peacock feathers')
		self.check_comment('sibuk tapi santai')
		self.add_list_item('Use peacock feathers to make a fly')

		# There is still a text box inviting her to add another item. She
		# enters "Use peacock feathers to make a fly" (Edith is very
		# methodical)
		self.add_list_item('Use peacock feathers to make a fly')

		# The page updates again, and now shows both items on her list
		self.wait_for_row_in_list_table('2: Use peacock feathers to make a fly')
		self.add_list_item('Use peacock feathers to make a fly')
		self.add_list_item('Use peacock feathers to make a fly')
		self.add_list_item('Use peacock feathers to make a fly')
		self.check_comment('oh tidak')

		# Satisfied, she goes back to sleep
	

	def test_multiple_users_can_start_lists_at_different_urls(self):
		# Edith starts a new to-do list
		self.browser.get(self.live_server_url)
		self.add_list_item('Buy peacock feathers')		

		# She notices that her list has a unique URL
		edith_list_url = self.browser.current_url
		self.assertRegex(edith_list_url, '/lists/.+')		

		# Now a new user, Francis, comes along to the site.
		## We use a new browser session to make sure that no information
		## of Edith's is coming through from cookies etc
		self.browser.quit()
		self.browser = webdriver.Firefox()
		
		# Francis visits the home page.  There is no sign of Edith's
		# list
		self.browser.get(self.live_server_url)
		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('Buy peacock feathers', page_text)
		self.assertNotIn('make a fly', page_text)

		# Francis starts a new list by entering a new item. He
		# is less interesting than Edith...
		self.add_list_item('Buy milk')


		# Francis gets his own unique URL
		francis_list_url = self.browser.current_url
		self.assertRegex(francis_list_url, '/lists/.+')
		self.assertNotEqual(francis_list_url, edith_list_url)
		# Again, there is no trace of Edith's list
		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('Buy peacock feathers', page_text)
		self.assertIn('Buy milk', page_text)
		# Satisfied, they both go back to sleep