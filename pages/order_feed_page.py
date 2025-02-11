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
        self.element_is_displayed(OrderFeedPageLocators.SEARCH_COUNTER_OF_ALL_TIME_IN_FEED)
        all_element_text = self.get_text_from_element(OrderFeedPageLocators.SEARCH_COUNTER_OF_ALL_TIME_IN_FEED)
        return all_element_text

    def get_orders_count_today(self):
        self.scroll_into_view(OrderFeedPageLocators.SEARCH_COUNTER_FOR_TODAY_IN_FEED)
        self.element_is_displayed(OrderFeedPageLocators.SEARCH_COUNTER_FOR_TODAY_IN_FEED)
        today_element_text = self.get_text_from_element(OrderFeedPageLocators.SEARCH_COUNTER_FOR_TODAY_IN_FEED)
        return today_element_text

    def get_orders_in_progress(self):
        self.element_is_displayed(OrderFeedPageLocators.SEARCH_ORDERS_IN_WORK_DONE)
        self.find_element_with_wait(OrderFeedPageLocators.SEARCH_ORDERS_IN_WORK_DONE)
        self.wait_disappear_element(OrderFeedPageLocators.SEARCH_ORDERS_IN_WORK_DONE)
        element_text = self.get_text_from_element(OrderFeedPageLocators.SEARCH_ORDER_IN_WORK)
        return element_text

    def wait_for_order_id_in_progress(self):
        order_id = 'Все текущие заказы готовы!'
        while order_id == 'Все текущие заказы готовы!':
            order_id = self.get_text_from_element(OrderFeedPageLocators.SEARCH_ORDER_IN_WORK)
        return order_id

    def check_order_id_in_progress(self):
        element_text = self.get_text_from_element(OrderFeedPageLocators.SEARCH_ORDER_IN_WORK)
        return element_text

    def check_order_id_in_feed(self):
        self.element_is_displayed(OrderFeedPageLocators.SEARCH_ORDER_ID_IN_FEED)
        element_text =  self.get_text_from_element(OrderFeedPageLocators.SEARCH_ORDER_ID_IN_FEED)
        return element_text.lstrip('#')
