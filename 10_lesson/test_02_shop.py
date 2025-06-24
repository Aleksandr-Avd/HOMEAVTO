import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from Shop.login_page import LoginPage
from Shop.inventory_page import InventoryPage
from Shop.cart_page import CartPage
from Shop.checkout_page import CheckoutPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

@allure.feature("Покупка товаров")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Проверка покупки товаров с итоговой суммой")
@allure.description("Тестирует полный сценарий покупки товаров на сайте saucedemo.com")
def test_purchase_flow(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    with allure.step("Открыть сайт и авторизоваться"):
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

    with allure.step("Добавить товары в корзину"):
        inventory_page.add_item_to_cart()

    with allure.step("Переход в корзину"):
        inventory_page.go_to_cart()

    with allure.step("Переход к оформлению заказа"):
        cart_page.click_checkout()

    with allure.step("Заполняем форму оформления заказа"):
        checkout_page.fill_checkout_info("Иван", "Петров", "123456")
        checkout_page.click_continue()

    with allure.step("Проверяем итоговую сумму"):
        total = checkout_page.get_total()
        with allure.step(f"Итоговая сумма: {total}"):
            assert total == "58.29", f"Итоговая сумма не совпадает, ожидается 58.29, получено {total}"