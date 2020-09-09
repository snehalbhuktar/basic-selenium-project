 # Verify the element state -> Enabled/Dissabled
 # You can only work on the "Enabled" elements, so always make sure that the element you are finding has Enabled status

import os

from selenium import webdriver
from selenium.webdriver.common.by import By


class ElementState():

    def __init__(self):
        caps = {'browserName': os.getenv('BROWSER', 'chrome')}
        self.browser = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities=caps
        )

    def test_isEnabled(self):
        browser = self.browser
        # Maximise window
        browser.maximize_window()
        # Open the URL of the application under test
        baseURL = "https://www.google.com/"
        browser.get(baseURL)
        browser.implicitly_wait(5)

        e1 = browser.find_element_by_css_selector("input.gLFyf")
        e1State = e1.is_enabled()
        print("Is web element enabled: " + str(e1State))

        e1.send_keys("test")

result = ElementState()
result.test_isEnabled()  