import os
import time
import unittest

from selenium import webdriver
import HtmlTestRunner

class CruiseLinkTest(unittest.TestCase):

    def setUp(self):
        caps = {'browserName': os.getenv('BROWSER', 'chrome')}
        self.browser = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities=caps
        )

    def test_cruise_link_verification(self):
        browser = self.browser
        browser.implicitly_wait(30)
        #Open the test URL
        browser.get('http://newtours.demoaut.com')
        browser.find_elements_by_xpath('//a[contains(text(),"Cruises")]').click()
        #Verify the next page navigation with title 'Cruises: Mercury Tours'
        if browser.title == 'Cruises: Mercury Tours':
            print('Test passed')
            browser.find_element_by_link_text('Cruises').click()

    def tearDown(self):
        self.browser.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./reports'))