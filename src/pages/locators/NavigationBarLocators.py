from selenium.webdriver.common.by import By


class NavigationBarLocators :

    COMPANY_MENU = (By.XPATH, "//a[@id='navbarDropdownMenuLink' and contains(text(),'Company')]")
    CAREERS_SUB_MENU = (By.XPATH, "//a[@class='dropdown-sub' and contains(text(),'Careers')]")

