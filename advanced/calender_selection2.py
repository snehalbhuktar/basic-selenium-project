# Select date from calender

import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By



class CalenderSelection2():

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
        baseURL = "https://www.expedia.com"
        browser.get(baseURL)
        browser.implicitly_wait(30)

        # Find the check in date field
        browser.find_element_by_id("d1-btn").click()
        # Find month
        calMonth = browser.find_element_by_xpath("//div[@class='uitk-new-date-picker-month']//h2[contains(text(),'September 2020')]")
        validDates = calMonth.find_element(By.TAG_NAME, 'button')

        time.sleep(3)
        for date in validDates:

            if date.text == '30':
                date.click()
                break


result = CalenderSelection2()
result.test()