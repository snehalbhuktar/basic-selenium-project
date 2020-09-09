# Verification of Hidden Element

import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By



class HiddenElements():

    def __init__(self):
        caps = {'browserName': os.getenv('BROWSER', 'chrome')}
        self.browser = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities=caps
        )

    def test_LetsKodeIt(self):
        browser = self.browser

        # Maximise window
        browser.maximize_window()

        # Open the URL of the application under test
        baseURL = "https://letskodeit.teachable.com/p/practice"
        browser.get(baseURL)
        browser.implicitly_wait(3)

        # Find the state of the text box
        textBoxElement = browser.find_element_by_id("displayed-text")
        textBoxState = textBoxElement.is_displayed()      # Returns True if visible, returns False if not visible, 
        #exception when not present in DOM
        print("Text box visible? " + str(textBoxState))

        # Click on the Hide button
        hideBtn = browser.find_element_by_id("hide-textbox")
        hideBtn.click()

        # Verify the state of the text box again
        textBoxState = textBoxElement.is_displayed()      # Returns True if visible, returns False if not visible, 
        #exception when not present in DOM
        print("Text box visible? " + str(textBoxState))

        # Click on the Show button
        showBtn = browser.find_element_by_id("show-textbox")
        showBtn.click()

        ## Verify the state of the text box again
        textBoxState = textBoxElement.is_displayed()     # Returns True if visible, returns False if not visible, 
        #exception when not present in DOM
        print("Text box visible? " + str(textBoxState))

        # Close the browser
        browser.quit()

    


result = HiddenElements()
result.test_LetsKodeIt()