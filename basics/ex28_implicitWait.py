# Implicit wait

import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By



class ImplicitWait():

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

        # Login to the application
        browser.find_element_by_link_text("Login").click()
        email = browser.find_element_by_id("user_email")
        email.send_keys("test@email.com")



result = ImplicitWait()
result.test()