# Select element from the suggested list of elements

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
        baseURL = "https://www.southwest.com"
        browser.get(baseURL)
        browser.implicitly_wait(10)

        # Find Depart field to enter partial data
        departField = browser.find_element_by_id("LandingAirBookingSearchForm_originationAirportCode")
        departField.send_keys("New York")

        time.sleep(3)

        # Find the element and click
        itemToSelect = 


