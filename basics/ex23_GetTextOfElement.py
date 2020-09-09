# Get text of the element

import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By



class GetText():

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
        browser.get(baseURL)
        browser.implicitly_wait(5)

        el1 = browser.find_element_by_id("opentab")
        elementText = el1.text
        print("Text of the element is: " + elementText)

        time.sleep(1)
        browser.quit()


result = GetText()
result.test()
