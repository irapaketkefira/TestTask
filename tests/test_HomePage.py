
import pytest

from src.pages.CareersPage import CareersPage
from src.pages.NavigationBar import NavigationBar
from src.pages.HomePage import HomePage
from src.pages.CookieBanner import CookieBanner
from src.pages.locators.CareersPageLocators import CareersPageLocators

@pytest.mark.usefixtures("web_driver")

class TestHomePage:

    def test_home_page_is_opened(self):
        home_page = HomePage(self.driver)
        cookie_banner = CookieBanner(self.driver)
        home_page.go_to_home_page()
        cookie_banner.accept_cookie()
        home_page.verify_home_page_is_opened()

    def test_navigate_to_career_page(self):
        navigation_bar = NavigationBar(self.driver)
        careers_page = CareersPage(self.driver)
        navigation_bar.open_career_page_though_navigation_bar()
        careers_page.verify_section_is_visible('Location')
        careers_page.verify_section_is_visible('Team')
        careers_page.verify_section_is_visible('Life at insider')






