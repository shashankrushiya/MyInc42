from config.config import Config
from utilities.dynamic_wait import wait_helper
from datetime import datetime


class SeleniumWrapper:

    def __init__(self, driver):
        self.driver = driver

    @wait_helper
    def element_present(self, locator):
        self.driver.find_element(*locator)

    @wait_helper
    def click(self, locator):
        self.driver.find_element(*locator).click()

    @wait_helper
    def input_text(self, locator, *, value):
        self.driver.find_element(*locator).send_keys(value)

    def get_screenshot(self, screenshot_name):
        today = datetime.now()
        self.driver.save_screenshot(Config.SCREENSHOTS_PATH + f"{screenshot_name}-{today.day}-{today.hour}-{today.minute}.png")

