#Verify - user should be able to open a new  Checking account

import time
import unittest
import os

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import HtmlTestRunner

class Open_NewAccount1_test(unittest.TestCase):

    def setUp(self):
        caps = {'browserName': os.getenv('BROWSER', 'chrome')}
        self.browser = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities=caps
        )

    def test_open_new_account_ckecking(self):
        browser = self.browser
        browser.maximize_window()
        browser.get('https://parabank.parasoft.com/parabank/admin.htm')
        #Enter the newly registered username & password
        username = browser.find_element_by_name('username')
        username.send_keys('ajit25')
        password = browser.find_element_by_name('password')
        password.send_keys('root1111')
        browser.find_element_by_class_name('button').click()
        #verify Account Overview page
        if browser.title == 'ParaBank | Accounts Overview':
            #print('Test passed')
            browser.find_element_by_link_text('Open New Account').click()

            #Open new account page will be opened
            if browser.title == 'Open New Account':
                #Select the account type as 'CHECKING'
                account_type = browser.find_element_by_xpath('//select[@id="type"]')
                account_type.select_by_value('0')
                #Select the From account
                account_num = browser.find_element_by_xpath('//select[@id="fromAccountId"]')
                account_num.select_by_value('13677')
                #Click on Open new account button
                browser.find_element_by_xpath('/input[@class="button"]').click()
                #Verify the success message
                self.assertIn('Congratulations, your account is now open.', browser.page_source)


        

    def tearDown(self):
        self.browser.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./reports'))

