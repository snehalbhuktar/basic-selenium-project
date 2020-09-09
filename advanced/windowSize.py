import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By



class WindowSize():

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
        baseURL = "https://letskodeit.teachable.com"
        browser.get(baseURL)
        browser.implicitly_wait(10)

        # Use java script execution to get height and width
        height = browser.execute_script("return window.innerHeight;")
        width = browser.execute_script("return window.innerWidth;")

        print("Height is: " + str(height))
        print("Width is: " + str(width))

        browser.quit()


result = WindowSize()
result.test()