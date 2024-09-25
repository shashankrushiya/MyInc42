import pytest
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from config.config import Config


@pytest.fixture()
def driver_(request):
    # Set up the Firefox driver using webdriver-manager
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    # Navigating to given URL
    driver.get(Config.BASE_URL)

    # Maximize window for better visibility
    driver.maximize_window()

    yield driver

    # Tear down the browser after the tests
    driver.quit()
