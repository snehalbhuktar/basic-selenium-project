# Explicit wait

import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *



class ExplicitWait():

    def __init__(self):
        caps = {'browserName': os.getenv('BROWSER', 'chrome')}
        self.browser = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities=caps
        )

    def waitForElement(self, locator, locatorType = "id", timeout=10, pollfrequency=0.5):
        element = None
        try:
            print("Wating for maximum " + str(timeout) + " seconds for element to be clickable")
            wait = WebDriverWait(self.browser, 10, poll_frequency=1,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException])
        element = wait.until(EC.element_to_be_clickable((By.ID,
                                                         "stopFilter_stops-0")))
        print("Element appeared on the web page")
        except:
            print("Element not appeared on the web page")
            print_stack()
        return element
