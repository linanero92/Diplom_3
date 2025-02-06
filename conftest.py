import pytest
from selenium import webdriver
import urls
import data
from selenium.webdriver.firefox.options import Options

@pytest.fixture(params=[data.browser_chrome, data.browser_firefox])
def driver(request, driver):
    options = Options()
    if request.param == data.browser_chrome:
        data.DRIVER_NAME = data.browser_chrome
        driver = webdriver.Chrome()
    elif request.param == data.browser_firefox:
        data.DRIVER_NAME = data.browser_firefox
        driver = webdriver.Firefox(options=options)
    driver.get(urls.MAIN_PAGE_URL)
    yield webdriver
    driver.quit()






