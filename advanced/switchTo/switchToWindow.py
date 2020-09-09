import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By



class SwitchToWindow():

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

        # Find the parent handle -> current window
        parentHandle = browser.current_window_handle
        print("PArent handlw: " + str(parentHandle))
        time.sleep(3)

        # Click on the Open window button
        browser.find_element_by_id("openwindow").click()
        time.sleep(4)

        # Find all the handles, there are two handles after clicking open window button
        handles = browser.window_handles

        # Switch to other window
        for handle in handles:
            print("Handle: " + handle)
            if handle not in parentHandle:
                browser.switch_to.window(handle)
                print("Switched to window: " + handle)
                searchField = browser.find_element_by_id("placeholder")
                searchField.send_keys("Java")
                time.sleep(2)
                browser.close()
                break
        
        # Switch to parent window
        browser.switch_to.window(parentHandle)
        browser.find_element_by_id("name").send_keys("test")

result = SwitchToWindow()
result.test()