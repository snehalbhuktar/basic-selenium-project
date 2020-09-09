# Get attribte of the element

import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By



class GetAttribute():

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

        el = browser.find_element_by_id("name")
        attribute1 = el.get_attribute("class")
        print("Attribute of the element is: " + attribute1)
        
        attribute2 = el.get_attribute("type")
        print("Attribute of the element is: " + attribute2)

        attribute3 = el.get_attribute("name")
        print("Attribute of the element is: " + attribute3)

        time.sleep(2)
        browser.quit()


result = GetAttribute()
result.test()