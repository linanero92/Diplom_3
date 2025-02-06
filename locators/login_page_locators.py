SEARCH_LOGIN_BUTTON = (By.XPATH, '//form[contains(@class, "Auth_form")]//button[text()="Войти"]')
SEARCH_ERROR_INVALID_PASSWORD = (
    By.XPATH, '//div[contains(@class, "input__container")]//p[text()="Некорректный пароль"]')
SEARCH_LOGIN_EMAIL_INPUT = (By.XPATH,
                            '//div[contains(@class, "Auth_login")]//div[contains(@class, "input__container")]//input[@type="text" and @name="name"]')
SEARCH_LOGIN_PASSWORD_INPUT = (By.XPATH,
                               '//div[contains(@class, "Auth_login")]//div[contains(@class, "input__container")]//input[@type="password" and @name="Пароль"]')
