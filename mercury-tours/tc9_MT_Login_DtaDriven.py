#Data Driven test for Login scenario
#Verify the Login scenario with set of data which includes valid and invalid users


import os
import time
import unittest
from MTUsers import writeData
from MTUsers import readData
from MTUsers import getRowCount

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import HtmlTestRunner
import logging

#path = '/home/snehal/selenium-python/selenium practice/mercury tours'

logging.basicConfig(filename="login_data_driven.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

    #Creating an object
logger=logging.getLogger()

#Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)

class LoginDDTest(unittest.TestCase):

    def setUp(self):
        caps = {'browserName': os.getenv('BROWSER', 'chrome')}
        self.browser = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities=caps
        )

    def test_login_data_driven(self):
        browser = self.browser
        browser.maximize_window()
        #Path where the external file with users details is saved
        filepath = '/home/snehal/selenium-python/selenium practice/mercury tours/Users.xlsx'
        
        #Open the Test URL
        browser.get('http://newtours.demoaut.com')
        
        #Login with set of usename and password
        rows = getRowCount(filepath, 'sheet1')
        # logging.debug("Rows: %d", rows)

        for r in range(2, rows+1):
            tc_username = readData(filepath, 'sheet1', r, 1)
            tc_password = readData(filepath, 'sheet1', r, 2)
            browser.find_element_by_name('userName').send_keys(tc_username)
            browser.find_element_by_name('password').send_keys(tc_password)
            # logging.debug("Username: %s", tc_username)
            # logging.debug("Password: %s", tc_password)
            browser.find_element_by_name('login').click()
            
            if browser.title == 'Find a Flight: Mercury Tours: ':
                writeData(filepath, 'sheet1', r, 3, 'Test Passed')
            
            else:
                writeData(filepath, 'sheet1', r, 3, 'Test Failed')

            browser.find_element_by_link_text('Home').click()
    
    def tearDown(self):
        self.browser.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./reports'))
