import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import requests
import urls
import data
from helpers import Generator


@pytest.fixture(params=[data.browser_chrome, data.browser_firefox])
def driver(request):
    if request.param == data.browser_chrome:
        data.DRIVER_NAME = data.browser_chrome
        options = ChromeOptions()
        driver = webdriver.Chrome(options=options)
    elif request.param == data.browser_firefox:
        data.DRIVER_NAME = data.browser_firefox
        options = FirefoxOptions()
        driver = webdriver.Firefox(options=options)
    else:
        raise ValueError(f"Unsupported browser: {request.param}")

    driver.maximize_window()
    driver.get(urls.MAIN_PAGE_URL)
    yield driver
    driver.quit()


@pytest.fixture
def create_new_user_and_delete():
    email = Generator.generate_random_email(5)
    password = Generator.generate_random_string(7)
    name = Generator.generate_random_string(7)

    payload = {
        "email": email,
        "password": password,
        "name": name
    }

    auth_data = [email, password, name]
    response = requests.post(urls.USER_REGISTER_ENDPOINT, json=payload)
    response_json = response.json()
    token = response_json.get('accessToken')
    yield auth_data, token
    headers = {'Authorization': token[1]}
    requests.delete(urls.USER_DELETE_ENDPOINT, headers=headers)

