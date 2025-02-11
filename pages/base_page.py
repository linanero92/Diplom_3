import allure
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains


class BasePage:

    @allure.step('Инициализация веб-драйвера')
    def __init__(self, driver):
        self.driver = driver

    def wait_for_visibility(self, locator):
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Поиск элемента')
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 8).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Отображение эдемента')
    def check_displaying_of_element(self, locator):
        return self.find_element_with_wait(locator).is_displayed()

    @allure.step('Кликабельность элемента')
    def check_element_is_clickable(self, locator):
        WebDriverWait(self.driver, 15).until(expected_conditions.element_to_be_clickable(locator))
        return self.find_element_with_wait(locator)

    def wait_for_modal_closed(self, driver, locator):
        wait = WebDriverWait(driver, 3)
        try:
            element = wait.until(expected_conditions.invisibility_of_element_located(locator))
            return element
        except TimeoutException:
            print("Modal did not close within the expected time")

    @allure.step('Клик по элементу')
    def click_to_element(self, locator):
        WebDriverWait(self.driver, 15).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    @allure.step('Добавление текста в элемент')
    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    @allure.step('Получение текста из элемента')
    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    @allure.step('Скролл до элемента')
    def scroll_into_view_js(self, locator):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", locator)

    def wait_disappear_element(self, locator):
        WebDriverWait(self.driver, 100).until(expected_conditions.invisibility_of_element_located(locator))

    def scroll_into_view(self, locator):
        element = self.find_element_with_wait(locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    @allure.step('Форматирование локатора')
    def format_locators(self, locator, num):
        return [locator[0], locator[1].format(num)]

    @allure.step("Получение текущего URL")
    def get_current_url(self):
        return self.driver.current_url

    def element_is_displayed(self, locator):
        return self.find_element_with_wait(locator).is_displayed()

    def move_the_element(self, locator_element, locator_target):
        element = self.find_element_with_wait(locator_element)
        target = self.find_element_with_wait(locator_target)
        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(element, target).perform()

    def drag_and_drop_element(self, source_locator, target_locator):
        source_element = self.find_element_with_wait(source_locator)
        target_element = self.find_element_with_wait(target_locator)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(source_element, target_element).perform()

        script = """
        function simulateDragDrop(sourceNode, destinationNode) {
            var EVENT_TYPES = {
                DRAG_END: 'dragend',
                DRAG_START: 'dragstart',
                DROP: 'drop'
            }

            function createCustomEvent(type) {
                var event = new CustomEvent("CustomEvent")
                event.initCustomEvent(type, true, true, null)
                event.dataTransfer = {
                    data: {
                    },
                    setData: function(type, val) {
                        this.data[type] = val
                    },
                    getData: function(type) {
                        return this.data[type]
                    }
                }
                return event
            }

            function dispatchEvent(node, type, event) {
                if (node.dispatchEvent) {
                    return node.dispatchEvent(event)
                }
                if (node.fireEvent) {
                    return node.fireEvent("on" + type, event)
                }
            }

            var event = createCustomEvent(EVENT_TYPES.DRAG_START)
            dispatchEvent(sourceNode, EVENT_TYPES.DRAG_START, event)

            var dropEvent = createCustomEvent(EVENT_TYPES.DROP)
            dropEvent.dataTransfer = event.dataTransfer
            dispatchEvent(destinationNode, EVENT_TYPES.DROP, dropEvent)

            var dragEndEvent = createCustomEvent(EVENT_TYPES.DRAG_END)
            dragEndEvent.dataTransfer = event.dataTransfer
            dispatchEvent(sourceNode, EVENT_TYPES.DRAG_END, dragEndEvent)
        }
        simulateDragDrop(arguments[0], arguments[1]);
        """
        self.driver.execute_script(script, source_element, target_element)

    def js_button_click(self, element):
        self.driver.execute_script("arguments[0].click();", element)

