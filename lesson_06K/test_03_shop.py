import pytest
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_03_shop():
    driver = webdriver.Firefox(service=FirefoxService(
        GeckoDriverManager(version="v0.34.0").install()
    ))

    try:
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        waiter = WebDriverWait(driver, 10)

        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        driver.find_element(By.NAME, "add-to-cart-sauce-labs-backpack").click()
        driver.find_element(
            By.NAME, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        driver.find_element(By.NAME, "add-to-cart-sauce-labs-onesie").click()

        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        driver.find_element(By.ID, "checkout").click()

        driver.find_element(By.ID, "first-name").send_keys("Ekaterina")
        driver.find_element(By.ID, "last-name").send_keys("Andrievskaya")
        driver.find_element(By.ID, "postal-code").send_keys("859684")
        driver.find_element(By.ID, "continue").click()

        waiter.until(EC.text_to_be_present_in_element(
            (By.CLASS_NAME, "summary_total_label"), "$58.29"))

        total_element = driver.find_element(
            By.CLASS_NAME, "summary_total_label")
        assert total_element.text == "Total: $58.29"

    finally:
        driver.quit()

