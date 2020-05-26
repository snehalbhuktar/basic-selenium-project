#Verify the Login scenario with incorrect credentials
#User should not be able to login with incorrect username and password

import time
import unittest
import os

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import HtmlTestRunner

class Login_Failure_test(unittest.TestCase):

    def setUp(self):
        caps = {'browserName': os.getenv('BROWSER', 'chrome')}
        self.browser = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities=caps
        )

    def test_login_failure(self):
        browser = self.browser
        browser.maximize_window()
        browser.get('https://parabank.parasoft.com/parabank/admin.htm')
        #Enter the newly registered username & password
        username = browser.find_element_by_name('username')
        username.send_keys('fgfd')
        password = browser.find_element_by_name('password')
        password.send_keys('root1111')
        browser.find_element_by_class_name('button').click()
        #verify Account Overview page
        if browser.title == 'ParaBank | Error':
            print('Test passed')


        
    def tearDown(self):
        self.browser.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./reports'))
