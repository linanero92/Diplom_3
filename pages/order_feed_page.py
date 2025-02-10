import allure
from pages.base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPageLocators


class OrderFeedPage(BasePage):

    def check_feed_title_text(self):
        return self.get_text_from_element(OrderFeedPageLocators.SEARCH_FEED_TITLE_TEXT)

    def click_to_order(self):
        self.check_element_is_clickable(OrderFeedPageLocators.SEARCH_MADE_ORDER)
        self.click_to_element(OrderFeedPageLocators.SEARCH_MADE_ORDER)

    def get_order_details_text(self):
        return self.get_text_from_element(OrderFeedPageLocators.SEARCH_ORDER_DETAILS_TEXT)

    def get_orders_count_all_time(self):
        element_text = self.get_text_from_element(OrderFeedPageLocators.SEARCH_COUNTER_OF_ALL_TIME_IN_FEED)
        return element_text

