from selenium.webdriver.common.by import By

class MainPageLocators:

    SEARCH_LOGIN_BUTTON_VIA_MAINPAGE = \
        (By.XPATH, '//section[2]//button[contains(text(), "Войти в аккаунт")]')