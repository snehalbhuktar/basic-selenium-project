import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains



class MouseHover():

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

        browser.execute_script("window.scrollBy(0, 500);")
        time.sleep(2)
        element = browser.find_element_by_id("mousehover")
        elementToClick = "//div[@class='mouse-hover-content']//a[text()='Top']"
        
        try:
            actions = ActionChains(browser)
            actions.move_to_element(element).perform()
            print("Mouse hovered on element")
            time.sleep(2)
            topLink = browser.find_element_by_xpath(elementToClick)
            # topLink.click() or can use "actions" to perform the click
            actions.move_to_element(topLink).click().perform()
            print("Item clicked")
        except:
            print("Mouse hovered failed on element")



result = MouseHover()
result.test()
