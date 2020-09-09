# Verification of Click() and send_keys() methods

import os
import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
import HtmlTestRunner


class ClickAndSendKeys():

    def setUp(self):
        caps = {'browserName': os.getenv('BROWSER', 'chrome')}
        self.browser = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities=caps
        )

    def test(self):
        browser = self.browser
        # Maximise window
        browser.maximize_window()
        # Open the URL of the application under test
        baseURL = "https://letskodeit.teachable.com"
        browser.get(baseURL)
        browser.implicitly_wait(10)

        login_link = browser.find_element_by_xpath("//a[@class='navbar-link fedora-navbar-link']")
        login_link.click()

        email = browser.find_element_by_id("user_email")
        email.send_keys("test")
        password = browser.find_element_by_id("user_password")
        password.send_keys("test")

        time.sleep(30)

        # To clear the text field
        email.clear()

        time.sleep(3)
        email.send_keys("test")


    def tearDown(self):
        self.browser.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./reports'))


#result = ClickAndSendKeys()
#result.test()  

    