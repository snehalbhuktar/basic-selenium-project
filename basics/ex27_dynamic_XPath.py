# Dynamic XPath format

import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By



class DynamicXPathFormat():

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
        baseURL = "https://letskodeit.teachable.com/p/practice"
        browser.get(baseURL)
        browser.implicitly_wait(5)

        # Login to the application
        browser.find_element_by_link_text("Login").click()
        email = browser.find_element_by_id("user_email")
        email.send_keys("test@email.com")
        password = browser.find_element_by_id("user_password")
        password.send_keys("abcabc")
        browser.find_element_by_name("commit").click()

        #Search for course
        searchCourse = browser.find_element_by_id("search-courses")
        searchCourse.send_keys("JavaScript")

        # Select course
        # XPath for course"Java script fot brginner" - //div[contains(@class, 'course-listing-title') and contains(text(), 'JavaScript for beginners')]
        _course = "//div[contains(@class, 'course-listing-title') and contains(text(),'{0}')]"
        _courseLocator = _course.format("JavaScript for beginners")

        courseElement = browser.find_element(By.XPATH, _courseLocator)
        courseElement.click()



aa = DynamicXPathFormat()
aa.test()