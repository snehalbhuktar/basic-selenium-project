#Verify the registration failure scenario
#When mandatory fields are left empty, error message will be displayed

import os
import time
import unittest

from selenium import webdriver
import HtmlTestRunner

class Register_WithError_test(unittest.TestCase):

    def setUp(self):
        caps = {'browserName': os.getenv('BROWSER', 'chrome')}
        self.browser = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities=caps
        )

    def test_register_with_error(self):
        browser = self.browser
        browser.maximize_window()
        browser.get('https://parabank.parasoft.com/parabank/admin.htm')
        #Click on the Register link
        browser.find_element_by_link_text('Register').click()
        self.assertIn('Signing up is easy!', browser.page_source)
        #Fill up the registration form
        first_name = browser.find_element_by_id('customer.firstName')
        first_name.send_keys('aamba')
        last_name = browser.find_element_by_id('customer.lastName')
        last_name.send_keys('1234')
        address = browser.find_element_by_id('customer.address.street')
        address.send_keys('baner')
        city = browser.find_element_by_id('customer.address.city')
        city.send_keys('pune')
        state = browser.find_element_by_id('customer.address.state')
        state.send_keys('goa')
        #Dont enter values in the remaining fields, click on Register and verify the error message
        browser.find_element_by_xpath('//table[@class="form2"]//input[@class="button"]  ').click()
        self.assertIn('Zip Code is required.', browser.page_source)
        #error_id = browser.find_element_by_id('customer.ssn.errors')
        #self.assertEqual(error_id, browser.page_source)
        

    def tearDown(self):
        self.browser.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./reports'))
