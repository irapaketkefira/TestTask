from selenium.webdriver.common.by import By

class OpenPositionsLocators():

    ACCEPT_ALL_BUTTON = (By.CSS_SELECTOR,'a#wt-cli-accept-all-btn')
    SEE_ALL_QA_JOBS_BUTTON = (By.XPATH, "//a[contains(text(),'See all QA jobs')]")
    LOCATION_FILTER = (By.CSS_SELECTOR, "span#select2-filter-by-location-container")
    LOCATION_FILTER_ISTANBUL_OPTION = (By.XPATH, "//li[@class='select2-results__option' and contains(text(),'Istanbul')]")
    DEPARTMENT_FILTER = (By.XPATH,"//span[@title='Quality Assurance']")
    QA_POSITION = (By.XPATH,"//li[@class='select2-results__option' and contains(text(),'Quality Assurance')]")
    OPEN_POSITION_SECTION = (By.CSS_SELECTOR, 'section#career-position-list')
    POSITION = (By.CSS_SELECTOR, 'div[class="position-list-item-wrapper bg-light"]')
    VIEW_ROLE_BUTTON = (By.XPATH, '//a[contains(text(),"View Role")]')