
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class SeleniumExtended:

    def __init__(self, driver):
        self.driver = driver
        self.default_timeout = 15


    def wait_and_click(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout

        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
            # EC.element_to_be_clickable(locator)
        ).click()


    def wait_until_element_is_visible(self, locator_or_element, timeout=None):
        timeout = timeout if timeout else self.default_timeout

        if isinstance(locator_or_element, tuple):
            elem = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator_or_element)
            )
        else:
            import selenium.webdriver.remote.webelement
            if isinstance(locator_or_element, selenium.webdriver.remote.webelement.WebElement):
                elem = WebDriverWait(self.driver, timeout).until(
                    EC.visibility_of(locator_or_element)
                )
            else:
                raise TypeError(f"The locator to check visibility must be a 'tuple' or a 'WebElement'. It was {type(locator_or_element)}")

        return elem


    def wait_until_elements_are_visible(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout

        elem = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_all_elements_located(locator)
        )

        return elem

    def focus_element(self, locator, timeout=None):
        element = self.driver.find_element(*locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        actions.perform()