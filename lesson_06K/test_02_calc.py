import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_02_calc():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))

    try:
        url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"  # noqa
        driver.get(url)

        waiter = WebDriverWait(driver, 50)

        delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys("45")

        buttons = driver.find_elements(By.CSS_SELECTOR, ".keys span")
        buttons[0].click()  # 7
        buttons[3].click()  # +
        buttons[1].click()  # 8
        buttons[14].click()  # =

        waiter.until(EC.text_to_be_present_in_element(
            (By.CLASS_NAME, "screen"), "15"))

        screen_element = driver.find_element(By.CLASS_NAME, "screen")
        assert screen_element.text == "15"

    finally:
        driver.quit()

