from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class LoginPage:
    """
    Класс для работы со страницей авторизации.
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы.

        :param driver: WebDriver для управления браузером
        """
        self.driver = driver
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def open(self) -> None:
        """
        Открыть страницу авторизации.
        """
        self.driver.get("https://www.saucedemo.com/")

    def enter_username(self, username: str) -> None:
        """
        Ввести имя пользователя.

        :param username: имя пользователя
        """
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self, password: str) -> None:
        """
        Ввести пароль.

        :param password: пароль пользователя
        """
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login(self) -> None:
        """
        Нажать кнопку входа.
        """
        self.driver.find_element(*self.login_button).click()

    def login(self, username: str, password: str) -> None:
        """
        Выполнить полный вход.

        :param username: имя пользователя
        :param password: пароль пользователя
        """
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()