import time
from datetime import datetime
from config.config import Config
from pages.home_page import HomePage
from pages.datalabs_page import DatalabsPage
from pages.login_page import LoginPage
from pages.search_page import SearchPage


def test_login_search(driver_):

    # Home Page interactions
    homepage = HomePage(driver_)
    homepage.click_datalabs()

    # Datalabs Page interactions
    datalabs_page = DatalabsPage(driver_)
    datalabs_page.click_login()

    # Login Page interactions
    login_page = LoginPage(driver_)
    login_page.login()

    # Perform search and capture results
    search_page = SearchPage(driver_)
    search_page.check_dashboard_element()
    search_page.perform_search("fintech")
    search_page.verify_search_results()
