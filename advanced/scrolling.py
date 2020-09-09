import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By



class ScollingPage():

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
        browser.implicitly_wait(10)

        #Scroll down - using java script execution
        browser.execute_script("window.scrollBy(0, 1000);") # 0 for horizontal, 1000 for vertical
        time.sleep(3)

        #Scroll up - using java script execution
        browser.execute_script("window.scrollBy(0, -1000);") # 0 for horizontal, -1000 for vertical
        time.sleep(3)

        #Scroll to view element
        element = browser.find_element_by_id("mousehover")
        browser.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(3)
        browser.execute_script("window.scrollBy(0, -100);")

        # Native way to scroll element to view
        browser.execute_script("window.scrollBy(0, -1000);")
        location = element.location_once_scrolled_into_view
        print("Location is: " + str(location))



result = ScollingPage()
result.test()