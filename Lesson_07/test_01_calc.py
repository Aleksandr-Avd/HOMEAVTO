import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from Calc.calculation import CalcPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

def test_calculator(driver):
     calculator_page = CalcPage(driver)
     calculator_page.open()
     calculator_page.set_delay("45")
     calculator_page.click_button_7()
     calculator_page.click_button_plus()
     calculator_page.click_button_8()
     calculator_page.click_button_equals()
     calculator_page.expect()
     result = calculator_page.get_result()
     assert result == "15", f"Результат не равен 15, получено: {result}"