#Verify the Registration failure scenario
#User is not able to register with duplicate username

import time
import unittest
import os

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import HtmlTestRunner

class Register_DuplicateCredentialsError_test(unittest.TestCase):

    def setUp(self):
        caps = {'browserName': os.getenv('BROWSER', 'chrome')}
        self.browser = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities=caps
        )

    def test_register_duplicate_credentials_error(self):
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
        zipcode = browser.find_element_by_id('customer.address.zipCode')
        zipcode.send_keys('1062PK')
        ssn = browser.find_element_by_id('customer.ssn')
        ssn.send_keys('98765432')
        username = browser.find_element_by_id('customer.username')
        username.send_keys('komal')
        password = browser.find_element_by_id('customer.password')
        password.send_keys('abcd12')
        confirmpassword = browser.find_element_by_id('repeatedPassword')
        confirmpassword.send_keys('abcd12')
        browser.find_element_by_class_name('button').click()
        #WebDriverWait(browser, 30)
        #time.sleep(3)
        #msgerror = browser.find_element_by_id('customer.username.errors')
        #target1 = browser.find_element_by_class_name('error')
        #target1 = browser.find_element_by_css_selector('#customer.username.errors')
        #self.assertEqual('This username already exists.', target1.text)

        #This will capture error message
        actual_msg = browser.find_element_by_id('customer.username.errors').get_attribute('text')

        #Expected message
        expected_msg = 'This username already exists.'

        #Verify expected and actual results
        self.assertEquals(expected_msg, actual_msg)

    def tearDown(self):
        self.browser.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./reports'))

        