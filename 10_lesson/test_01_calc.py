import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from Calc.calculation import CalcPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

@allure.feature("Калькулятор с задержкой")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Тест сложения 7 + 8 с задержкой")
@allure.description("Проверяет, что калькулятор корректно считает 7 + 8 с задержкой 45 секунд.")
def test_calculator(driver):
    calculator_page = CalcPage(driver)

    with allure.step("Открываем страницу калькулятора"):
        calculator_page.open()

    with allure.step("Устанавливаем задержку 45 секунд"):
        calculator_page.set_delay("45")

    with allure.step("Вводим 7 + 8"):
        calculator_page.click_button_7()
        calculator_page.click_button_plus()
        calculator_page.click_button_8()

    with allure.step("Нажимаем кнопку равно"):
        calculator_page.click_button_equals()

    with allure.step("Ожидаем результат 15"):
        calculator_page.expect()

    with allure.step("Получаем и проверяем результат"):
        result = calculator_page.get_result()
        assert result == "15", f"Результат не равен 15, получено: {result}"