import allure
from helpers import Generator
from locators.password_recovery_locators import PasswordRecoveryLocators
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class PasswordRecoveryPage(BasePage):

    def click_go_to_login_button(self):
        self.check_element_is_clickable(MainPageLocators.SEARCH_LOGIN_BUTTON_VIA_MAINPAGE)
        self.click_to_element(MainPageLocators.SEARCH_LOGIN_BUTTON_VIA_MAINPAGE)

    def click_to_recovery_password_link(self):
        self.check_element_is_clickable(PasswordRecoveryLocators.SEARCH_PASSWORD_RECOVERY_LINK_VIA_LOGIN_PAGE)
        self.click_to_element(PasswordRecoveryLocators.SEARCH_PASSWORD_RECOVERY_LINK_VIA_LOGIN_PAGE)

    def enter_email_to_recovery_password(self):
        generator = Generator()
        self.check_element_is_clickable(PasswordRecoveryLocators.SEARCH_EMAIL_INPUT_VIA_PASSWORD_RECOVERY)
        self.click_to_element(PasswordRecoveryLocators.SEARCH_EMAIL_INPUT_VIA_PASSWORD_RECOVERY)
        self.add_text_to_element(PasswordRecoveryLocators.SEARCH_RECOVERY_EMAIL_INPUT_FOCUSED,
                                 generator.generate_random_email(5))
        self.click_to_element(PasswordRecoveryLocators.SEARCH_RECOVERY_PASSWORD_BUTTON)

    def check_password_recovery_field(self):
        return self.get_text_from_element(PasswordRecoveryLocators.SEARCH_RECOVERY_PASSWORD_INPUT)

    def check_password_recovery(self):
        self.click_go_to_login_button()
        self.click_to_recovery_password_link()
        self.enter_email_to_recovery_password()

    def click_password_make_visible_hidden(self):
        self.check_element_is_clickable(PasswordRecoveryLocators.SEARCH_ICON_PASSWORD_RECOVERY_MAKE_VISIBLE)
        self.click_to_element(PasswordRecoveryLocators.SEARCH_ICON_PASSWORD_RECOVERY_MAKE_VISIBLE)

    def enter_new_password(self):
        self.check_element_is_clickable(PasswordRecoveryLocators.SEARCH_RECOVERY_ENTER_NEW_PASSWORD_FOCUSED)
        self.click_to_element(PasswordRecoveryLocators.SEARCH_RECOVERY_ENTER_NEW_PASSWORD_FOCUSED)
        generator = Generator()
        self.add_text_to_element(PasswordRecoveryLocators.SEARCH_RECOVERY_ENTER_NEW_PASSWORD_FOCUSED, generator.generate_random_string(8))

    def check_password_visible(self):
        return self.check_displaying_of_element(PasswordRecoveryLocators.PASSWORD_VISIBLE_FIELD_ACTIVE)

    def check_password_hidden(self):
        return self.check_displaying_of_element(PasswordRecoveryLocators.PASSWORD_HIDE_FIELD_NOT_ACTIVE)
