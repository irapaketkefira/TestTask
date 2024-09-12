from src.pages.locators.NavigationBarLocators import NavigationBarLocators
from src.SeleniumExtended import SeleniumExtended

class NavigationBar(NavigationBarLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def open_career_page_though_navigation_bar(self):
        self.sl.wait_and_click(self.COMPANY_MENU)
        self.sl.wait_and_click(self.CAREERS_SUB_MENU)
