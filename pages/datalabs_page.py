# pages/datalabs_page.py
from utilities.generic import SeleniumWrapper


class DatalabsPage(SeleniumWrapper):
    LOGIN_BUTTON = ("xpath", '//button[text()="Login"]')

    def click_login(self):
        self.click(self.LOGIN_BUTTON)
