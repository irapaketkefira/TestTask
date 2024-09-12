from src.pages.locators.HomePageLocators import HomePageLocators
from src.SeleniumExtended import SeleniumExtended
from src.helpers.config_helpers import get_base_url


class HomePage(HomePageLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_home_page(self):
        home_url = get_base_url()
        self.driver.get(home_url)

    def verify_home_page_is_opened(self):
        self.sl.wait_until_element_is_visible(self.DESCRIPTION_SECTION)

