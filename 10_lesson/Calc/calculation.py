from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver

class CalcPage:
    """
    Класс для работы со страницей калькулятора с задержкой.
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы.

        :param driver: WebDriver для управления браузером
        """
        self.driver = driver
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.button_7 = (By.XPATH, "//span[text()='7']")
        self.button_plus = (By.XPATH, "//span[text()='+']")
        self.button_8 = (By.XPATH, "//span[text()='8']")
        self.button_equals = (By.CSS_SELECTOR, ".btn-outline-warning")
        self.wait = WebDriverWait(driver, 46)
        self.result_display = (By.CSS_SELECTOR, ".screen")

    def open(self) -> None:
        """
        Открыть страницу калькулятора.
        """
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )

    def set_delay(self, delay: str) -> None:
        """
        Установить задержку вычисления.

        :param delay: задержка в секундах в виде строки, например "45"
        """
        delay_input_element = self.driver.find_element(*self.delay_input)
        delay_input_element.clear()
        delay_input_element.send_keys(delay)

    def click_button_7(self) -> None:
        """
        Нажать кнопку '7'.
        """
        self.driver.find_element(*self.button_7).click()

    def click_button_plus(self) -> None:
        """
        Нажать кнопку '+'.
        """
        self.driver.find_element(*self.button_plus).click()

    def click_button_8(self) -> None:
        """
        Нажать кнопку '8'.
        """
        self.driver.find_element(*self.button_8).click()

    def click_button_equals(self) -> None:
        """
        Нажать кнопку '='.
        """
        self.driver.find_element(*self.button_equals).click()

    def expect(self) -> None:
        """
        Ожидать, что в элементе с результатом появится текст '15'.
        """
        self.wait.until(
            EC.text_to_be_present_in_element(self.result_display, "15")
        )

    def get_result(self) -> str:
        """
        Получить текст результата.

        :return: результат вычисления в виде строки
        """
        return self.driver.find_element(*self.result_display).text