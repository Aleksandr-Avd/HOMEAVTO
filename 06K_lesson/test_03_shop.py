import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


def test_purchase_flow(driver):
    driver.get("https://www.saucedemo.com/")

    # Авторизация
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    
    # Добавляем товары в корзину
    items = [
        "add-to-cart-sauce-labs-backpack",
        "add-to-cart-sauce-labs-bolt-t-shirt",
        "add-to-cart-sauce-labs-onesie"]
    for item_id in items:
        driver.find_element(By.ID, item_id).click()

    # Переходим в корзину
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Нажимаем Checkout
    driver.find_element(By.ID, "checkout").click()

    # Заполняем форму
    driver.find_element(By.ID, "first-name").send_keys("Иван")
    driver.find_element(By.ID, "last-name").send_keys("Петров")
    driver.find_element(By.ID, "postal-code").send_keys("123456")

    driver.find_element(By.ID, "continue").click()

    # Читаем итоговую сумму
    total_text = driver.find_element(By.CLASS_NAME, "summary_total_label").text
    # Текст вида: "Total: \$58.29"
    total_value = total_text.split("$")[-1]

    assert total_value == "58.29", f"Итоговая сумма {total_value} не равна \$58.29"

    print (total_value)