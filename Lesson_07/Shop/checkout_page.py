from selenium.webdriver.common.by import By

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.postal_code_input = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_label = (By.CLASS_NAME, "summary_total_label")

    def fill_checkout_info(self, first_name, last_name, postal_code):
        # Заполняем форму оформления заказа
        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(*self.postal_code_input).send_keys(postal_code)

    def click_continue(self):
        # Нажимаем кнопку Continue
        self.driver.find_element(By.ID, "continue").click()

    def get_total(self):
        # Получаем итоговую стоимость
        total_text = self.driver.find_element(*self.total_label).text  # Пример: "Total: \$58.29"
        return total_text.split("$")[1].strip()    
    