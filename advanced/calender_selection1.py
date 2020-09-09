# Select date from calender

import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By



class CalenderSelection():

    def __init__(self):
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
        baseURL = "https://www.skyscanner.nl/?previousCultureSource=COOKIE&redirectedFrom=www.skyscanner.net"
        browser.get(baseURL)
        browser.implicitly_wait(40)

        # Find the Depart date field
        browser.find_element_by_css_selector("#depart-fsc-datepicker-button").click()
        # Find date to be selected
        depart_date = browser.find_element_by_xpath("//button[@title='Departure date']//span[contains(text(),'25')]")
        depart_date.click()

        print("Depart date is: " + str(depart_date))

        time.sleep(3)
        browser.quit()


result = CalenderSelection()
result.test()


