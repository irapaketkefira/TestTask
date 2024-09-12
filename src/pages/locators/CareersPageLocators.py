from selenium.webdriver.common.by import By

class CareersPageLocators:

    FIND_YOUR_DREAM_JOB_BUTTON = (By.XPATH, '(//div/a[contains(text(),"Find your dream job")])[1]')
    LOCATIONS_SECTION = (By.CSS_SELECTOR, '#career-our-location')
    TEAMS_SECTION = (By.XPATH, '//*[@data-id="efd8002"]')
    LIFE_AT_INSIDER_SECTION = (By.XPATH,'//*[@data-id="a8e7b90"]')