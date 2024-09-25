# pages/search_page.py
import time

from utilities.generic import SeleniumWrapper


class SearchPage(SeleniumWrapper):
    DASHBOARD_ELEMENT = ("xpath", '//button[@class="join-inc42-button"]')
    SEARCH_FIELD = ('id', "global_search")
    KEYWORD = "Fintech"
    SEARCH_RESULT = ('id', "datalabs-search-result")

    def __init__(self, driver):
        super().__init__(driver)

    def check_dashboard_element(self):
        try:
            try:
                my_inc42_button = self.element_present(self.DASHBOARD_ELEMENT)
            except Exception as E:
                print(E)
            print("Dashboard element found: MyInc42 link")
            print("Login Successful")
            self.get_screenshot("login_successful")

        except Exception as E:
            print(E)
            print("Dashboard Element not found")
            print("Login Failure")
            self.get_screenshot("login failure")

    def perform_search(self, keyword):
        self.input_text(self.SEARCH_FIELD, value=self.KEYWORD)
        time.sleep(5)

    def verify_search_results(self):
        try:
            companies_dashboard = self.element_present(self.SEARCH_RESULT)
            print("Search Results verified for keyword: Fintech")
            self.get_screenshot("search_results")
        except Exception as E:
            print("Failed to search due to", {E})
            self.get_screenshot("search_failed")
