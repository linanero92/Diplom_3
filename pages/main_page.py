from locators.main_page_locators import MainPageLocators
from locators.order_feed_page_locators import OrderFeedPageLocators
from pages.base_page import BasePage
from pages.account_page import AccountPage
import data


class MainPage(BasePage):

    def click_login_button(self):
        self.check_element_is_clickable(MainPageLocators.SEARCH_LOGIN_BUTTON_VIA_MAINPAGE)
        self.click_to_element(MainPageLocators.SEARCH_LOGIN_BUTTON_VIA_MAINPAGE)

    def click_account_button(self):
        self.check_element_is_clickable(MainPageLocators.SEARCH_PERSONAL_ACCOUNT_LINK)
        self.click_to_element(MainPageLocators.SEARCH_PERSONAL_ACCOUNT_LINK)

    def click_constructor_link(self):
        self.check_element_is_clickable(MainPageLocators.SEARCH_CONSTRUCTOR)
        self.click_to_element(MainPageLocators.SEARCH_CONSTRUCTOR)

    def get_constructor_from_account_page(self):
        account_page = AccountPage(self.driver)
        if data.DRIVER_NAME == data.browser_firefox:
            account_page.close_modal()
        self.click_account_button()
        self.click_account_button()
        self.click_constructor_link()

    def get_feed_after_login(self):
        account_page = AccountPage(self.driver)
        if data.DRIVER_NAME == data.browser_firefox:
            account_page.close_modal()
        self.get_feed()
        self.get_feed()

    def check_constructor_title(self):
        return self.get_text_from_element(MainPageLocators.SEARCH_CONSTRUCTOR_TITLE_TEXT)

    def get_feed(self):
        self.check_element_is_clickable(MainPageLocators.SEARCH_FEED_VIA_MAIN_PAGE)
        self.click_to_element(MainPageLocators.SEARCH_FEED_VIA_MAIN_PAGE)

    def get_ingredient_details(self):
        self.check_element_is_clickable(MainPageLocators.SEARCH_INGREDIENT_DETAILS)
        self.click_to_element(MainPageLocators.SEARCH_INGREDIENT_DETAILS)

    def check_ingredient_title_text(self):
        return self.get_text_from_element(MainPageLocators.SEARCH_INGREDIENT_DETAILS_MODAL_TITLE)

    def close_ingredient_details_modal(self):
        self.check_element_is_clickable(MainPageLocators.SEARCH_INGREDIENT_DETAILS_MODAL_CLOSE)
        self.click_to_element(MainPageLocators.SEARCH_INGREDIENT_DETAILS_MODAL_CLOSE)

    def check_ingredient_details_modal_closed(self):
        return self.get_text_from_element(MainPageLocators.SEARCH_SAUCES_SECTION)

    def check_count_before_ingredient_added(self):
        return self.get_text_from_element(MainPageLocators.SEARCH_COUNTER_INGREDIENT_NOT_ADDED)

    def add_ingredient(self):
        self.check_element_is_clickable(MainPageLocators.SEARCH_FIRST_BUN_IN_CONSTRUCTOR)
        self.check_element_is_clickable(MainPageLocators.SEARCH_TARGET_BASKET)
        if data.DRIVER_NAME == data.browser_chrome:
            self.move_the_element(MainPageLocators.SEARCH_FIRST_BUN_IN_CONSTRUCTOR, MainPageLocators.SEARCH_TARGET_BASKET)
        elif data.DRIVER_NAME == data.browser_firefox:
            self.drag_and_drop_element(MainPageLocators.SEARCH_FIRST_BUN_IN_CONSTRUCTOR,
                                       MainPageLocators.SEARCH_TARGET_BASKET)
    def check_count_after_ingredient_added(self):
        return self.get_text_from_element(MainPageLocators.SEARCH_COUNTER_INGREDIENT_ADDED)

    def click_make_order_button(self):
        self.check_element_is_clickable(MainPageLocators.SEARCH_MAKE_ORDER_BUTTON)
        self.click_to_element(MainPageLocators.SEARCH_MAKE_ORDER_BUTTON)

    def check_order_id_text(self):
        return self.get_text_from_element(MainPageLocators.SEARCH_ORDER_ID_TEXT)

    def make_order(self):
        self.add_ingredient()
        self.click_make_order_button()
