#Verify the link 'Forget login info?'
# Click on the link 'Forget login info?', enter the details and get the login information

import time
import unittest
import os

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import HtmlTestRunner

class Forgot_LoginInfo_test(unittest.TestCase):

    def setUp(self):
        caps = {'browserName': os.getenv('BROWSER', 'chrome')}
        self.browser = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities=caps
        )

    def test_forgot_login_info(self):
        browser = self.browser
        browser.maximize_window()
        browser.get('https://parabank.parasoft.com/parabank/admin.htm')
        
        #Click on the link 'Forget login info?'
        browser.find_element_by_link_text('Forgot login info?').click()
        
        #Enter the details
        first_name = browser.find_element_by_id('firstName')
        first_name.send_keys('user')
        last_name = browser.find_element_by_id('lastName')
        last_name.send_keys('manage')
        address = browser.find_element_by_id('address.street')
        address.send_keys('baner')
        city = browser.find_element_by_id('address.city')
        city.send_keys('pune')
        state = browser.find_element_by_id('address.state')
        state.send_keys('goa')
        zipcode = browser.find_element_by_id('address.zipCode')
        zipcode.send_keys('1062PK')
        ssn = browser.find_element_by_id('ssn')
        ssn.send_keys('123456789')
        browser.find_element_by_xpath('//table[@class="form2"]//input[@class="button"]').click()

        self.assertIn('Your login information was located successfully. You are now logged in.', browser.page_source)

        #if browser.title == 'Customer Lookup':
            #print('Test passed')
        
    def tearDown(self):
        self.browser.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./reports'))
