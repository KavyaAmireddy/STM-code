import unittest
import time
from selenium import webdriver

class TestOne(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.PhantomJS()
		self.driver.set_window_size(1120, 550)

	def test_url(self):
		self.driver.get("http://jobs.kent.edu/cw/en-us/listing/")
		self.driver.find_element_by_id(
			'search-keyword').send_keys("Chemistry")
		time.sleep(6)
		self.assertIn(
			"http://jobs.kent.edu/cw/en-us/search/?search-keyword=Chemistry", self.driver.current_url
		)
		count=0
		jobtitle = self.driver.find_element_by_id('search-results-content').find_elements_by_tag_name('tr') 
		for info in jobtitle: 
			row = info.find_elements_by_tag_name('td') 
			for data in row[0:5]: 
			    if(count == 0): 
			        print('****************') 
			    print(data.text) 
			    count = count+1 
			count = 0
	

	def tearDown(self):
		self.driver.quit()

if __name__ == '__main__':
	unittest.main()