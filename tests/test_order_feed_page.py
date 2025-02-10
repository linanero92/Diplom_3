import allure
from pages.order_feed_page import OrderFeedPage
from pages.login_page import LoginPage
from pages.main_page import MainPage


class TestOrderFeedPage:

    def test_get_order_details(self, driver):
        main_page = MainPage(driver)
        main_page.get_feed()
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.click_to_order()
        expected_result = 'Cостав'
        assert order_feed_page.get_order_details_text() == expected_result
