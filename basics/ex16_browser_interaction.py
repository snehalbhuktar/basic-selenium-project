# Verify the browser interactions using different methods


import os

from selenium import webdriver
from selenium.webdriver.common.by import By


class BrowserInteraction():

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

        # Get the title of the web page
        title = browser.title
        print("The title of the web page is: " + title)

        # Get current URL
        currentURL = browser.current_url
        print("Current URL is: " + currentURL)

        # Refresh the page
        browser.refresh
        print("Web page refreshed for the first time")
        browser.get(browser.current_url)
        print("Web page refreshed second time")

        #Open the another URL
        browser.get("https://sso.teachable.com/secure/42299/users/sign_in?clean_login=true&reset_purchase_session=1")
        # Browser back
        browser.back()
        print("Go one step back in the browser history")

        # Browser forward
        browser.forward()
        print("Go one step forward in the browser history")

        # Get the page source
        browser.page_source

        # Close/Quit the browser
        # Close -> closes the current browser.
        # Quit -> Closes all the browsers
        browser.close()
        browser.quit()


        


result = BrowserInteraction()
result.test()  