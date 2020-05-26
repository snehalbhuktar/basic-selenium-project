#Verify the navigation to the Account details page

import time
import unittest
import os

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import HtmlTestRunner

class Verify_AccountDetails_test(unittest.TestCase):

    def setUp(self):
        caps = {'browserName': os.getenv('BROWSER', 'chrome')}
        self.browser = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities=caps
        )

    def test_verify_account_details(self):
        browser = self.browser
        browser.maximize_window()
        browser.get('https://parabank.parasoft.com/parabank/admin.htm')
        #Enter the newly registered username & password
        username = browser.find_element_by_xpath('//input[@name="username"] ')
        username.send_keys('komal')
        password = browser.find_element_by_xpath('//input[@name="password"]')
        password.send_keys('abcd12')
        browser.find_element_by_xpath('//div[@class="login"]//input[@class="button"]  ').click()
        #verify Account Overview page
        homepage = browser.find_element_by_class_name('title')
        self.assertEqual('Accounts Overview', homepage.text)
        #Verify account details
        browser.find_element_by_class_name('ng-binding').click()
        page = browser.find_element_by_class_name('title')
        #page = browser.find_element_by_xpath('//h1[contains(text(),"Account Details")]  ')
        self.assertEqual('Account Details', page.text)
        #accnum = browser.find_element_by_id('accountId')
        #self.assertEqual('13677', accnum.text)
        #accounttype = browser.find_element_by_id('accountType')
        #self.assertEqual('CHECKING', accounttype.text)

    def tearDown(self):
        self.browser.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./reports'))
