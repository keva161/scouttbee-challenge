from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest

"""
This file contains the fixture which will be run before the tests.

Webdriver_Manager is used to ensure the latest version of the driver executables are being used.

"""

@pytest.fixture
def browser():

    # The following options block will start up Chrome without notifications enabled that could interfere with our test.

    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.add_experimental_option("prefs", prefs)

    b = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

    # Implicit waits are not advised. But including one here for demo purposes

    b.implicitly_wait(10)
    yield b
    b.quit()