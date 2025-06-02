from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.checkout_button = (By.ID, "checkout")

    def click_checkout(self):
        # Нажимаем кнопку Checkout
        self.driver.find_element(By.ID, "checkout").click()