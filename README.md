# Диплом - часть 3.
# Автоматизированное UI тестирование веб-приложения Stellar Burgers с использованием patterna Page Object 

## Использованные библиотеки:

- pytest
- Selenium WebDriver
- requests
- allure

### Структура проекта

- `page` - здесь описаны методы
- `tests` - пакет, содержащий тесты

### Запуск автотестов

**Установка зависимостей**

> `$ pip install -r requirements.txt`

**Запуск автотестов и создание allure-отчета**

>  `$ pytest tests/ --alluredir=allure_results`

**Просмотр allure-отчета в браузере**

>  `$ allure serve allure_results`


