# Verify the selecion of radio buttons and checkbox

import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class RadioButton_CheckBox():

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

        bmwRadioBtn = browser.find_element_by_id("bmwradio")
        bmwRadioBtn.click()

        time.sleep(3)
        hondaRadioBtn = browser.find_element_by_id("hondaradio")
        hondaRadioBtn.click()

        time.sleep(3)
        bmwCheckbox = browser.find_element_by_id("bmwcheck")
        bmwCheckbox.click()

        time.sleep(3)
        benzCheckbox = browser.find_element_by_id("benzcheck")
        benzCheckbox.click()

        # Returns "True" if selected, "False" if not selected
        print("BMW radio button is selected? " + str(bmwRadioBtn.is_selected()))
        print("Honda radio button is selected? " + str(hondaRadioBtn.is_selected()))
        print("BMW check box is selected? " + str(bmwCheckbox.is_selected()))
        print("Benz check box is selected? " + str(benzCheckbox.is_selected()))


result = RadioButton_CheckBox()
result.test()  