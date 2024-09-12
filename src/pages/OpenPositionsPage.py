import time
from logging import raiseExceptions

from src.pages.locators.OpenPositionsLocators import OpenPositionsLocators
from src.SeleniumExtended import SeleniumExtended
from src.helpers.config_helpers import get_base_url
from selenium.webdriver.common.by import By

class OpenPositionsPage(OpenPositionsLocators):

    endpoint = '/careers/quality-assurance/'

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_qa_open_positions_page(self):
        base_url = get_base_url()
        position_page_url = base_url + self.endpoint
        self.driver.get(position_page_url)
        self.sl.wait_and_click(self.ACCEPT_ALL_BUTTON)

    def click_on_see_all_qa_jobs_button(self):
        self.sl.wait_and_click(self.SEE_ALL_QA_JOBS_BUTTON)

    # //TODO: create step for selecting option from dropdown
    # def get_filter_location(self, filter_type):
    #     existing_filter_type = ['department', 'location']
    #
    #     if filter_type.lower() not in existing_filter_type:
    #         raise Exception(f"Provided filter '{filter_type}' is not exist on this page"
    #                         f"Existing sections are: {existing_filter_type}")
    #
    #     if filter_type.lower() == 'department':
    #         return self.DEPARTMENT_FILTER
    #     elif filter_type.lower() == 'location':
    #         return self.LOCATION_FILTER
    #
    #
    # def select_option_in_filter(self, filter_type, option):
    #     # self.driver.find_element('CSS_SELECTOR', self.LOCATION_FILTER)
    #     self.sl.wait_and_click(self.get_filter_location(filter_type))
    #     self.sl.wait_and_click([By.XPATH, "//li[contains(text(),'" + option + "')])"])
        # self.sl.wait_and_click(self.LOCATION_FILTER_ISTANBUL_OPTION)

    def select_istanbul_location(self):
        self.sl.wait_and_click(self.LOCATION_FILTER)
        self.sl.wait_and_click(self.LOCATION_FILTER_ISTANBUL_OPTION)

    def check_department(self):
        self.sl.wait_until_element_is_visible(self.DEPARTMENT_FILTER)

    def verify_position_list_is_shown(self):
        self.sl.focus_element(self.OPEN_POSITION_SECTION)
        self.driver.find_element(*self.OPEN_POSITION_SECTION)

    def get_positions(self):
        position_list = self.sl.wait_until_elements_are_visible(self.POSITION)
        return position_list

    def click_on_view_role_button(self):
        self.sl.focus_element(self.POSITION)
        self.sl.wait_and_click(self.VIEW_ROLE_BUTTON,20)

    def get_new_tab_url(self):
        original_window = self.driver.current_window_handle

        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break

        return self.driver.current_url

