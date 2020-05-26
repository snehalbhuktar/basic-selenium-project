import os
import time
import unittest

from selenium import webdriver
import HtmlTestRunner

class RegisterTest(unittest.TestCase):

    def setUp(self):
        caps = {'browserName': os.getenv('BROWSER', 'chrome')}
        self.browser = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities=caps
        )

    def test_register(self):
        browser = self.browser
        browser.implicitly_wait(30)
        browser.get('http://newtours.demoaut.com')
        #Click on the Register link
        browser.find_element_by_link_text('Register here').click()
        self.assertIn('REGISTER', browser.page_source)
        #Enter the details for registration
        Name1_box = browser.find_element_by_name('firstName')
        Name1_box.send_keys('snehal')
        Name2_box = browser.find_element_by_name('lastName')
        Name2_box.send_keys('bhuktar')
        address_box = browser.find_element_by_name('address1')
        address_box.send_keys('78 Aundh')
        city_box = browser.find_element_by_name('city')
        city_box.send_keys('Pune')
        postal_code = browser.find_element_by_name('postalCode')
        postal_code.send_keys('41156')
        #country = browser.find_element_by_name('country').click()
        #country.select_by_visible_text('India')
        user_name_box = browser.find_element_by_id('email')
        user_name_box.send_keys('temp1212@gmail.com')
        password_box = browser.find_element_by_name('password')
        password_box.send_keys('abc123')
        password2_box = browser.find_element_by_name('confirmPassword')
        password2_box.send_keys('abc123')
        #assert password_box == password2_box
        browser.find_element_by_name('register').click()
        self.assertIn('Thank you for registering', browser.page_source)
    
    def test_login(self):
        browser = self.browser
        browser.implicitly_wait(30)
        browser.get('http://newtours.demoaut.com')
        #Enter username and password for login
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