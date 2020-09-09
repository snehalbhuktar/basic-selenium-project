# Explicit wait

import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By



class ExplicitWait():

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
        # baseURL = "https://letskodeit.teachable.com/p/practice"
        browser.get(baseURL)
        
        browser.implicitly_wait(30)

        destination = browser.find_element(By.CSS_SELECTOR, "#location-field-destination-input")
        destination.send_keys("New York")



result = ExplicitWait()
result.test()




# uitk-button uitk-button-large uitk-button-fullWidth uitk-button-has-text uitk-button-primary
# uitk-layout-grid-item uitk-layout-grid-item-columnspan-small-1 uitk-layout-grid-item-columnspan-medium-2 