import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains



class SliderElement():

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
        baseURL = "https://jqueryui.com/slider"
        browser.get(baseURL)
        browser.implicitly_wait(5)

        browser.switch_to.frame(0)

        element = browser.find_element_by_xpath("//div[@id='slider']//span")

        try:
            actions = ActionChains(browser)
            actions.drag_and_drop_by_offset(element,70,0).perform()
            print("Sliding element successfully")
        except:
            print("Sliding element failed")


result = SliderElement()
result.test()