# Автоматизация тестирования калькулятора (PageObject + Allure)

## Описание

В проекте реализован Page Object для медленного калькулятора по адресу:  
https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html

Тест проверяет корректность сложения чисел 7 и 8 с задержкой 45 мс.

## Базовый синтаксис записи и форматирования

- Используйте [PEP 484](https://www.python.org/dev/peps/pep-0484/) для аннотации типов в методах.
- Комментарии и docstring оформляйте в формате reStructuredText или Google style.
- Allure шаги оформляйте с помощью `with allure.step("..."):` или декораторов `@allure.step`.
- В тестах добавляйте декораторы:
  - `@allure.title("...")` — заголовок теста
  - `@allure.description("...")` — описание теста
  - `@allure.feature("...")` — функциональная область
  - `@allure.severity(allure.severity_level.CRITICAL)` — уровень серьёзности

# Автоматизация тестирования магазина 

## Описание

Проект реализует UI-тесты для сайта [https://www.saucedemo.com/](https://www.saucedemo.com/) с использованием паттерна Page Object Model и Allure для отчетности.

В проекте каждый класс страницы находится в отдельной папке с `__init__.py` для удобного импорта.