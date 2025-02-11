from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):

    def click_to_recovery_password_link(self):
        self.check_element_is_clickable(LoginPageLocators.SEARCH_PASSWORD_RECOVERY_LINK_VIA_LOGIN_PAGE)
        self.click_to_element(LoginPageLocators.SEARCH_PASSWORD_RECOVERY_LINK_VIA_LOGIN_PAGE)

    def login_enter(self, email):
        self.add_text_to_element(LoginPageLocators.SEARCH_LOGIN_EMAIL_INPUT, email)

    def password_enter(self, password):
        self.add_text_to_element(LoginPageLocators.SEARCH_LOGIN_PASSWORD_INPUT, password)

    def login_button_click(self):
        self.check_element_is_clickable(LoginPageLocators.SEARCH_LOGIN_BUTTON)
        self.click_to_element(LoginPageLocators.SEARCH_LOGIN_BUTTON)

    def check_account_login(self, url):
        return self.get_current_url(url)

    def user_login(self, email, password):
        self.login_enter(email)
        self.password_enter(password)
        self.login_button_click()

    def get_login_button_text(self):
        return self.get_text_from_element(LoginPageLocators.SEARCH_LOGIN_BUTTON)
