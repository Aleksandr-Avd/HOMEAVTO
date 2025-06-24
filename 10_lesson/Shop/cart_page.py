from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class CartPage:
    """
    Класс для работы со страницей корзины.
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы.

        :param driver: WebDriver для управления браузером
        """
        self.driver = driver
        self.checkout_button = (By.ID, "checkout")

    def click_checkout(self) -> None:
        """
        Нажать кнопку Checkout.
        """
        self.driver.find_element(*self.checkout_button).click()