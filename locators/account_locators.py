from selenium.webdriver.common.by import By
class AccountLocators:

    SEARCH_PERSONAL_ACCOUNT_LINK = (
        By.XPATH, '//a[contains(@class, "AppHeader_header__link") and .//p[text()="Личный Кабинет"]]')