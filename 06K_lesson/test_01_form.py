import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys



def test_fill_form():
        driver = webdriver.Chrome(service =ChromeService(ChromeDriverManager().install()))
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        driver.find_element(By.NAME, "first-name").send_keys("Иван")
        driver.find_element(By.NAME, "last-name").send_keys("Петров")
        driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
        driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
        driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
        driver.find_element(By.NAME,"zip-code").send_keys("")   
        driver.find_element(By.NAME,"city").send_keys("Москва")
        driver.find_element(By.NAME, "country").send_keys("Россия")
        driver.find_element(By.NAME,"job-position").send_keys("QA")
        driver.find_element(By.NAME, "company").send_keys("SkyPro")
        
        driver.find_element(By.CLASS_NAME, "btn-outline-primary").click()
        pole_z = driver.find_element(By.ID, "zip-code").get_attribute("class")
        assert pole_z == "alert py-2 alert-danger"
        
        poles = ["#first-name", "#last-name", "#address", "#city", "#country", "#e-mail", "#phone", "#company"]
        for pole in poles:
                pole_class = driver.find_element(By.CSS_SELECTOR, pole).get_attribute("class")
                assert pole_class == "alert py-2 alert-success"
        
  