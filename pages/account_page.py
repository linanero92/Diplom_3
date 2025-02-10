import allure
import data
from locators.account_page_locators import AccountPageLocators
from pages.base_page import BasePage
from pages.login_page import LoginPage


class AccountPage(BasePage):

    def close_modal(self):
        try:
            self.find_element_with_wait(AccountPageLocators.SEARCH_MODAL_FF)
            if self.check_displaying_of_element(AccountPageLocators.SEARCH_MODAL_FF):
                close_button = self.find_element_with_wait(AccountPageLocators.SEARCH_MODAL_CLOSE_FOR_FF)
                self.click_to_element(close_button)
                self.wait_for_modal_closed(self.driver, AccountPageLocators.SEARCH_HEADER_ACCOUNT_PAGE)
        except Exception as e:
            print(f"Error closing modal: {e}")

    def get_account_page(self):
        if data.DRIVER_NAME == data.browser_firefox:
            self.close_modal()

    def check_logout_button(self):
        return self.get_text_from_element(AccountPageLocators.SEARCH_LOGOUT_BUTTON)

    def get_order_history(self):
        self.check_element_is_clickable(AccountPageLocators.SEARCH_ORDERS_HISTORY)
        self.click_to_element(AccountPageLocators.SEARCH_ORDERS_HISTORY)

    def logout_from_account(self):
        self.check_element_is_clickable(AccountPageLocators.SEARCH_LOGOUT_BUTTON)
        self.click_to_element(AccountPageLocators.SEARCH_LOGOUT_BUTTON)

    def check_order_history_url(self):
        return self.get_current_url()

    def check_login_url(self):
        return self.get_current_url()

    def get_login_button_from_login_page(self):
        login_page = LoginPage(self.driver)
        return login_page.get_login_button_text()
