# This is the code contains utilities


import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By



class HandyWrappers():

    def __init__(self):
        caps = {'browserName': os.getenv('BROWSER', 'chrome')}
        self.browser = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities=caps
        )

    def getByType(self, locatorType)
        locatorType = locatorType.lower()
        if locatorType = "id":
            return By.ID
        elif locatorType = "name":
            return By.NAME
        elif locatorType = "xpath":
            return By.XPATH
        elif locatorType = "css":
            return By.CSS_SELECTOR
        elif locatorType = "classname":
            return By.CLASS_NAME
        elif locatorType = "linktext":
            return By.LINK_TEXT
        else:
            print("Locator Type " + locatorType + " not supported")   

    def isElementPresent(self, locator, byType):
        try:
            element = self.browser.find_element(byType, locator)
            if element is not None:
                print("Element found")
                return True
            else:
                print("Element not found")
                return False

        except:
            print("Element not found")
            return False

    def elementPresenceCheck(self, locator, byType):
        try:
            elementList = self.browser.find_elements(byType, locator)
            if len(elementList) > 0:
                print("Elements found")
                return True
            else:
                print("Elements not found")
                return False
        except:
            print("Element not found")
            return False
        

