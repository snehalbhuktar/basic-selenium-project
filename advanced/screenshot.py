import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By



class Screenshot():

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

        # Click on the Login link and enter the details
        browser.find_element_by_link_text("Login").click()
        email = browser.find_element_by_id("user_email")
        email.send_keys("test@email.com")
        password = browser.find_element_by_id("user_password")
        password.send_keys("abc")
        browser.find_element_by_name("commit").click()

        time.sleep(3)

        destinationFileName = "/home/snehal/MyProject/udemy_Practice/test.png"
        
        try:
            browser.save_screenshot(destinationFileName)
            print("File is saved to the directory: " + str(destinationFileName))

        except NotADirectoryError:
            print("no error")


result = Screenshot()
result.test()
