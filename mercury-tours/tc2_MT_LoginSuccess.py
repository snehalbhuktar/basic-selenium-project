import os
import time
import unittest

from selenium import webdriver
import HtmlTestRunner

class LoginTest(unittest.TestCase):

    def setUp(self):
        caps = {'browserName': os.getenv('BROWSER', 'chrome')}
        self.browser = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities=caps
        )

    def test_login(self):
        browser = self.browser
        browser.implicitly_wait(30)
        #Open the test URL
        browser.get('http://newtours.demoaut.com')
        #Enter Username and Password on Home page for Login 
        username_field = browser.find_element_by_name('userName')
        username_field.send_keys('temp1212@gmail.com')
        password_field = browser.find_element_by_name('password')
        password_field.send_keys('abc123')
        browser.find_element_by_name('login').click()
        self.assertIn('findFlights', browser.page_source)
    
    def tearDown(self):
        self.browser.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./reports'))