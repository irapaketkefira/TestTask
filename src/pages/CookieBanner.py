from src.pages.locators.CookieBannerLocators import CookieBannerLocators
from src.SeleniumExtended import SeleniumExtended


class CookieBanner(CookieBannerLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def accept_cookie(self):
        self.sl.wait_and_click(self.ACCEPT_ALL_BUTTON)