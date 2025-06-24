from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class CheckoutPage:
    """
    Класс для работы со страницей оформления заказа.
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы.

        :param driver: WebDriver для управления браузером
        """
        self.driver = driver
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.postal_code_input = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_label = (By.CLASS_NAME, "summary_total_label")

    def fill_checkout_info(self, first_name: str, last_name: str, postal_code: str) -> None:
        """
        Заполнить форму оформления заказа.

        :param first_name: имя
        :param last_name: фамилия
        :param postal_code: почтовый индекс
        """
        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(*self.postal_code_input).send_keys(postal_code)

    def click_continue(self) -> None:
        """
        Нажать кнопку Continue.
        """
        self.driver.find_element(*self.continue_button).click()

    def get_total(self) -> str:
        """
        Получить итоговую сумму заказа.

        :return: строка с суммой (например "58.29")
        """
        total_text = self.driver.find_element(*self.total_label).text  # Пример: "Total: \$58.29"
        return total_text.split("$")[1].strip()