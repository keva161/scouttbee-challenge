"""
This file contains the methods and elements for interacting with the SauceDemo home page.
"""
from selenium.webdriver.common.by import By

class SauceDemoPage:

    def __init__(self, browser):
        self.browser = browser

    def GoTo(self):
        self.browser.get("https://www.saucedemo.com/")

    def HomePageTitle(self):
        return self.browser.title

    def Login(self):
        username_field = self.browser.find_element(By.ID, ("user-name"))
        password_field = self.browser.find_element(By.ID, ("password"))

        username_field.send_keys("standard_user")
        password_field.send_keys("secret_sauce")
        password_field.submit()