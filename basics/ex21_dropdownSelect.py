# To verify that user can select a value from drop down


import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class DropDownSelect():

    def __init__(self):
        caps = {'browserName': os.getenv('BROWSER', 'chrome')}
        self.browser = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities=caps
        )

    def test_SelectFromDropdown(self):
        browser = self.browser

        # Maximise window
        browser.maximize_window()

        # Open the URL of the application under test
        baseURL = "https://letskodeit.teachable.com/p/practice"
        browser.get(baseURL)
        browser.implicitly_wait(5)

        element = browser.find_element_by_id("carselect")
        sel = Select(element)

        sel.select_by_value("benz")
        print("Select Benz by value")
        time.sleep(2)

        sel.select_by_index("2")      # Passing the index as a string
        print("Select Hona by index")
        time.sleep(2)

        sel.select_by_visible_text("BMW")
        print("Select BMW by visible text")
        time.sleep(2)

        sel.select_by_index(2)       # Passing index as a integer
        print("Select Honda by index")


result = DropDownSelect()
result.test_SelectFromDropdown()  
