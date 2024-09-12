from src.pages.locators.CareersPageLocators import CareersPageLocators
from src.SeleniumExtended import SeleniumExtended
from selenium.webdriver.common.by import By


class CareersPage(CareersPageLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def get_section_locator(self, section_name):
        sections = ['location', 'team', 'life at insider']

        if section_name.lower() not in sections:
            raise Exception(f"Provided section '{section_name}' is not exist on this page"
                            f"Existing sections are: {sections}")

        if section_name.lower() == 'location':
            return self.LOCATIONS_SECTION
        elif section_name.lower() == 'team':
            return self.TEAMS_SECTION
        elif section_name.lower() == 'life at insider':
            return self.LIFE_AT_INSIDER_SECTION

    def click_on_find_you_dream_job_button(self):
        self.sl.wait_and_click(self.FIND_YOUR_DREAM_JOB_BUTTON)

    def verify_section_is_visible(self, section_name):
        # self.driver.find_element(By.CSS_SELECTOR, '#career-our-location')
        self.driver.find_element(*self.get_section_locator(section_name))