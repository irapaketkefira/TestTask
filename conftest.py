import pytest
from selenium import webdriver
import os

from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="class")
def web_driver(request):
    supported_browsers = ['chrome', 'ch', 'firefox', 'ff']
    browser = os.environ.get('BROWSER', None)
    if not browser:
        raise Exception ("The environment variable 'Browser' must be set. ")

    browser = browser.lower()
    if browser not in supported_browsers:
        raise Exception(f"Provided browser '{browser}' is not one of the supported."
                        f"Supported are: {supported_browsers}")

    chrome_options = Options()
    chrome_options.add_argument("--disable-search-engine-choice-screen")

    if browser in ('chrome', 'ch'):
        driver = webdriver.Chrome(options=chrome_options)
    elif browser in ('firefox', 'ff'):
        driver = webdriver.Firefox()

    request.cls.driver = driver
    yield
    # driver.quit()
