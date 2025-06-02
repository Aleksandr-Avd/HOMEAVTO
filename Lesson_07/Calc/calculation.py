from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalcPage:
    def __init__(self, driver):
        self.driver = driver
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.button_7 = (By.XPATH, "//span[text()='7']")
        self.button_plus = (By.XPATH, "//span[text()='+']")
        self.button_8 = (By.XPATH, "//span[text()='8']")
        self.button_equals = (By.CSS_SELECTOR, ".btn-outline-warning")
        self.wait = WebDriverWait(driver, 46)
        self.result_display = (By.CSS_SELECTOR, ".screen")

    def open(self):
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
            )

    def set_delay(self, delay):
        delay_input_element = self.driver.find_element(*self.delay_input)
        delay_input_element.clear()
        delay_input_element.send_keys(delay)

    def click_button_7(self):
        self.driver.find_element(*self.button_7).click()

    def click_button_plus(self):
        self.driver.find_element(*self.button_plus).click()

    def click_button_8(self):
        self.driver.find_element(*self.button_8).click()

    def click_button_equals(self):
        self.driver.find_element(*self.button_equals).click()

    def expect (self):
        result = self.wait.until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
        )

    def get_result(self):
        return self.driver.find_element(*self.result_display).text
        