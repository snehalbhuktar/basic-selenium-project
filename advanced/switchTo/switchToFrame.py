import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By



class SwitchToFrame():

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
        #Scroll down completely
        browser.execute_script("window.scrollBy(0, 1000);")

        # Switch to frame using id
        browser.switch_to.frame("courses-iframe")
        time.sleep(2)

        # Switch to frame using name
        #browser.switch_to.frame("iframe-name")

        # Switch to frame using number -> as only one frame is available, can be accessed by number 0
        #browser.switch_to.frame(0)  

        # Find the search box
        searchBox = browser.find_element_by_id("search-courses")
        searchBox.send_keys("python")
        time.sleep(2)

        #switch back to the parent frame
        browser.switch_to.default_content()
        browser.execute_script("window.scrollBy(0, -1000);")
        time.sleep(2)
        browser.find_element_by_id("name").send_keys("test")


result = SwitchToFrame()
result.test()