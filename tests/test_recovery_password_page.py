import allure
from pages.password_recovery_page import PasswordRecoveryPage


class TestPasswordRecoveryPage:

    def test_password_recovery(self, driver):
        password_recovery_page = PasswordRecoveryPage(driver)
        password_recovery_page.check_password_recovery()
        expected_result = 'Пароль'
        assert password_recovery_page.check_password_recovery_field() == expected_result

    def test_password_is_visible(self, driver):
        password_recovery_page = PasswordRecoveryPage(driver)
        password_recovery_page.check_password_recovery()
        password_recovery_page.enter_new_password()
        password_recovery_page.click_password_make_visible_hidden()
        assert password_recovery_page.check_password_visible()

    def test_password_is_hidden(self, driver):
        password_recovery_page = PasswordRecoveryPage(driver)
        password_recovery_page.check_password_recovery()
        password_recovery_page.enter_new_password()
        password_recovery_page.click_password_make_visible_hidden()
        password_recovery_page.click_password_make_visible_hidden()
        assert password_recovery_page.check_password_hidden()
