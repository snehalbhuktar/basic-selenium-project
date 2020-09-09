import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains



class DragAndDrop():

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
        baseURL = "https://jqueryui.com/droppable"
        browser.get(baseURL)
        browser.implicitly_wait(5)

        browser.switch_to.frame(0)
        fromElement = browser.find_element_by_id("draggable")
        toElement = browser.find_element_by_id("droppable")
        time.sleep(2)

        try:
            actions = ActionChains(browser)
            actions.click_and_hold(fromElement).move_to_element(toElement).release().perform()
            print("Drag and drop element sussfull")
        except:
            print("Drag and drop failed")



result = DragAndDrop()
result.test()


