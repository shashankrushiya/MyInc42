# pages/home_page.py
from utilities.generic import SeleniumWrapper


class HomePage(SeleniumWrapper):
    DATALABS_LINK = ("xpath", "//a[normalize-space()='Datalabs']")

    def __init__(self, driver):
        super().__init__(driver)

    def click_datalabs(self):
        self.click(self.DATALABS_LINK)
