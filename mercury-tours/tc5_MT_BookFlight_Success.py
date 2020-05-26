import os
import time
import unittest

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import HtmlTestRunner

class BookFlightTest(unittest.TestCase):

    def setUp(self):
        caps = {'browserName': os.getenv('BROWSER', 'chrome')}
        self.browser = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities=caps
        )

    def test_book_flight(self):
        browser = self.browser
        browser.maximize_window()
        #Open the Test URL
        browser.get('http://newtours.demoaut.com')
        #Login with valid usename and password
        username_field = browser.find_element_by_name('userName')
        username_field.send_keys('temp1212@gmail.com')
        password_field = browser.find_element_by_name('password')
        password_field.send_keys('abc123')
        browser.find_element_by_name('login').click()
        #Enter the details to book a flight
        browser.find_element_by_xpath('//body//b//input[1]').click()
        passengers_field = Select(browser.find_element_by_name("passCount"))
        passengers_field.select_by_value('2')
        departing_from_field = Select(browser.find_element_by_name('fromPort'))
        departing_from_field.select_by_value('London')
        departing_month_field = Select(browser.find_element_by_name('fromMonth'))
        departing_month_field.select_by_value('7')
        departing_day_field = Select(browser.find_element_by_name('fromDay'))
        departing_day_field.select_by_value('8')
        arriving_in_field = Select(browser.find_element_by_name('toPort'))
        arriving_in_field.select_by_value('Paris')
        arriving_month_field = Select(browser.find_element_by_name('toMonth'))
        arriving_month_field.select_by_value('7')
        arriving_day_field = Select(browser.find_element_by_name('toDay'))
        arriving_day_field.select_by_value('12')
        browser.find_element_by_xpath('//font[contains(text(),"Economy class")]').click()
        airline_field = Select(browser.find_element_by_name('airline'))
        airline_field.select_by_visible_text('No Preference')
        browser.find_element_by_name('findFlights').click()
        #Navigates to 'Select a Flight: Mercury Tours' page 
        #browser.find_element_by_name('outFlight').isSelected()
        #browser.find_element_by_name('inFlight').isSelected()
        browser.find_element_by_name('reserveFlights').click()
        #Check the summary page
        self.assertIn('Summary', browser.page_source)

        #Enter the details for purchase
        firstname = browser.find_element_by_name('passFirst0')
        firstname.send_keys('snehal')
        lastname = browser.find_element_by_name('passLast0')
        lastname.send_keys('bhuktar')
        cardnum = browser.find_element_by_name('creditnumber')
        cardnum.send_keys('0011223344')
        #Click on Secure purchase button
        browser.find_element_by_name('buyFlights').click()
        if browser.title == 'Flight Confirmation: Mercury Tours':
            print('Test passes. Booking confirmed')
            #Logout from the session
            browser.find_element_by_xpath('//td[3]//a[1]//img[1]').click()

    def tearDown(self):
        self.browser.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./reports'))