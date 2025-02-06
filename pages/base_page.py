import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains


class BasePage:

    @allure.step('Инициализация веб-драйвера')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Определение метода driver')
    def driver(self):
        driver = None
        return driver

    @allure.step('Ожидание открытия новой вкладки в браузере')
    def wait_for_window_opened(self, number):
        WebDriverWait(self.driver, 7).until(expected_conditions.number_of_windows_to_be(number))

    @allure.step('Поиск элемента')
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Клик по элементу')
    def click_to_element(self, locator):
        WebDriverWait(self.driver, 7).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    @allure.step('Добавление текста в элемент')
    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    @allure.step('Получение текста из элемента')
    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    @allure.step('Форматирование локатора')
    def format_locators(self, locator, num):
        return [locator[0], locator[1].format(num)]

    def move_the_element(self, locator_element, locator_target):
        element = self.find_element_with_wait(locator_element)
        target = self.find_element_with_wait(locator_target)
        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(element, target).perform()


    def drag_and_drop_element(self, source_element, target_element):
        script = """
            function simulateHTML5DragAndDrop(sourceNode, destinationNode) {
                var dataTransfer = new DataTransfer();
                var dragStartEvent = new DragEvent('dragstart', {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: dataTransfer
                    });
                    sourceNode.dispatchEvent(dragStartEvent);
                    var dropEvent = new DragEvent('drop', {
                        bubbles: true,
                        cancelable: true,
                        dataTransfer: dataTransfer
                    });
                    destinationNode.dispatchEvent(dropEvent);
                var dragEndEvent = new DragEvent('dragend', {
                        bubbles: true,
                        cancelable: true,
                        dataTransfer: dataTransfer
                    });
                    sourceNode.dispatchEvent(dragEndEvent);
                }
                simulateHTML5DragAndDrop(arguments[0], arguments[1]);
                """
        self.driver.execute_script(script, source_element, target_element)
