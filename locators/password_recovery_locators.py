SEARCH_PASSWORD_RECOVERY_LINK_VIA_LOGIN_PAGE = (
    By.XPATH, '//a[contains(@class, "Auth_link") and text()="Восстановить пароль"]')
SEARCH_LOGIN_EMAIL_INPUT_VIA_PASSWORD_RECOVERY = (By.XPATH,
                                                  '//form[contains(@class, "Auth_form")]//div[contains(@class, "input_type_text")]//input[@type="text" and @name="name"]')
SEARCH_RECOVERY_PASSWORD_BUTTON = (By.XPATH,
                                   '//form[contains(@class, "Auth_form")]//button[contains(@class, "button_button") and contains(@class, "button_button_type_primary") and text()="Восстановить"]')