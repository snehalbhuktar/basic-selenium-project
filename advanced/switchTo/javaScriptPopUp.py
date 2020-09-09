import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By



class ActionOnPopUp():

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
        baseURL = "https://letskodeit.teachable.com/pages/practice"
        browser.get(baseURL)
        browser.implicitly_wait(5)

        browser.find_element_by_id("name").send_keys("abcd")
        # Click on the alert button, and pop up appears
        browser.find_element_by_id("alertbtn").click()
        alert1 = browser.switch_to.alert
        # Click Ok on the pop up
        alert1.accept()
        time.sleep(2)

        browser.find_element_by_id("name").send_keys("abcd")
        # Click on the alert button, and pop up appears
        browser.find_element_by_id("confirmbtn").click()
        alert2 = browser.switch_to.alert
        # Click Cancel on the pop up
        alert2.dismiss()

result = ActionOnPopUp()
result.test()

