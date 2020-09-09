# Verify the presence of element on the web application

import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from udemy.handyWrappers import HandyWrappers

class ElementPresenceCheck():

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
        baseURL = "https://letskodeit.teachable.com/p/practice"
        browser.implicitly_wait(5)
        hw = HandyWrappers(browser)
        browser.get(baseURL)

        result = hw.isElementPresent("name", By.ID)
        print(str(result))


a = ElementPresenceCheck()
a.test

