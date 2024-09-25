# pages/login_page.py
from utilities.generic import SeleniumWrapper
from config.config import Config


class LoginPage(SeleniumWrapper):
    EMAIL_INPUT = ("id", '2-email')
    PASSWORD_INPUT = ("xpath", '//input[@type="password"]')
    LOGIN_BUTTON = ("name", 'submit')

    def __init__(self, driver):
        super().__init__(driver)

    def login(self):
        self.input_text(self.EMAIL_INPUT, value=Config.EMAIL)
        self.input_text(self.PASSWORD_INPUT, value=Config.PASSWORD)
        self.click(self.LOGIN_BUTTON)
