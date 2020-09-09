# Verify the list of elements
# Here we are checking how many radio buttons are available on the page and apply action on them



import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class ElementList():

    def __init__(self):
        caps = {'browserName': os.getenv('BROWSER', 'chrome')}
        self.browser = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities=caps
        )

    def test_ListOfElements(self):
        browser = self.browser

        # Maximise window
        browser.maximize_window()

        # Open the URL of the application under test
        baseURL = "https://letskodeit.teachable.com/p/practice"
        browser.get(baseURL)
        browser.implicitly_wait(5)

        radioButtonsList = browser.find_elements_by_xpath("//input[contains(@type,'radio') and contains(@name,'cars')]")
        size = len(radioButtonsList)
        print("Numbers of radio buttons available are: " + str(size))

        for button in radioButtonsList:
            isSelected = button.is_selected()

            if not isSelected:
                button.click()
                time.sleep(2) 



result = ElementList()
result.test_ListOfElements()  