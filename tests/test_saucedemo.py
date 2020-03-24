"""
These tests will cover the required functionality for our test.
"""

from pages.SauceDemoPage import SauceDemoPage


def test_saucedemo(browser):
    HomePage = SauceDemoPage(browser)

    TITLE = "Swag Labs"

    # Visits the homepage
    HomePage.GoTo()

    # Asserts the page title is as expected
    assert TITLE in HomePage.HomePageTitle()

    # Logs into the Demo Site
    HomePage.Login()

