from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class InventoryPage:
    """
    Класс для работы со страницей товаров.
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы.

        :param driver: WebDriver для управления браузером
        """
        self.driver = driver

    def add_item_to_cart(self) -> None:
        """
        Добавить несколько товаров в корзину.
        """
        items = [
            "add-to-cart-sauce-labs-backpack",
            "add-to-cart-sauce-labs-bolt-t-shirt",
            "add-to-cart-sauce-labs-onesie"
        ]
        for item_id in items:
            self.driver.find_element(By.ID, item_id).click()

    def go_to_cart(self) -> None:
        """
        Перейти в корзину.
        """
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()