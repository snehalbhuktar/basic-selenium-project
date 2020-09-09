# Find web element sing CSS selector
# Includes different methods to write CSS and to find unique matching node

import os

from selenium import webdriver
from selenium.webdriver.common.by import By


class FindElement_CSS():

    def __init__(self):
        caps = {'browserName': os.getenv('BROWSER', 'chrome')}
        self.browser = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities=caps
        )

    def test_find_element_CSS(self):
        browser = self.browser
        # Open the URL of the application under test
        #baseURL = "https://letskodeit.teachable.com/p/practice"
        browser.get("https://letskodeit.teachable.com/p/practice")

        # Find element by CSS -> syntax -> "#idvalue"
        elementCSS1 = browser.find_element_by_css_selector("#bmwradio")
        if elementCSS1 is not None:
            print("Element 1 found")

        # Find element by CSS -> syntax -> ".classvalue"
        elementCSS2 = browser.find_element_by_css_selector(".displayed-class")
        if elementCSS2 is not None:
            print("Element 2 found")

        # Find element by CSS -> syntax -> tag[attribute='value']
        elementCSS3 = browser.find_element_by_css_selector("a[id=opentab]")
        if elementCSS3 is not None:
            print("Element 3 found")

        # Find element by CSS -> syntax -> tag#idvalue
        elementCSS4 = browser.find_element_by_css_selector("input#bmwradio")
        if elementCSS4 is not None:
            print("Element 4 found")

        # Find element by CSS -> syntax -> tag.classvalue
        elementCSS5 = browser.find_element_by_css_selector("input.displayed-class")
        if elementCSS5 is not None:
            print("Element 5 found")

        # Find element by CSS - Appending classes -> syntax -> .class1.class2...
        elementCSS6 = browser.find_element_by_css_selector(".inputs.displayed-class")
        if elementCSS6 is not None:
            print("Element 6 found")

        # Find element by CSS - using wildcards -> syntax -> “^” -> Represents the starting text 
        elementCSS7 = browser.find_element_by_css_selector("input[onclick^='hide']")
        if elementCSS7 is not None:
            print("Element 7 found")

        # Find element by CSS - using wildcards -> syntax -> “$” -> Represents the ending text 
        elementCSS8 = browser.find_element_by_css_selector("input[id$='text']")
        if elementCSS8 is not None:
            print("Element 8 found")

        # Find element by CSS - using wildcards -> syntax -> “*” -> Represents the text contained 
        elementCSS9 = browser.find_element_by_css_selector("input[class*='displayed']")
        if elementCSS9 is not None:
            print("Element 9 found")
        


result = FindElement_CSS()
result.test_find_element_CSS()    
