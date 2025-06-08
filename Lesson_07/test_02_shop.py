import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

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

def test_purchase_flow(driver):
    # Открываем сайт магазина
    
    # Авторизация
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    
    # Добавление товаров в корзину
    inventory_page = InventoryPage(driver)
    inventory_page.add_item_to_cart()
    
   

    # Переход в корзину
    inventory_page.go_to_cart()
    # Нажатие Checkout
    cart_page = CartPage(driver)
    cart_page.click_checkout()

    # Заполнение формы оформления заказа
    checkout_page = CheckoutPage(driver)
    checkout_page.fill_checkout_info("Иван", "Петров", "123456")
    checkout_page.click_continue()

    # Проверка итоговой суммы
    total = checkout_page.get_total()
    assert total == "58.29", f"Итоговая сумма не совпадает, ожидается 58.29, получено {total}"