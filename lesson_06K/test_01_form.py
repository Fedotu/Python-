import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_01_form():
    service = EdgeService(
        executable_path=r"C:\Users\user\Downloads\msedgedriver.exe")
    driver = webdriver.Edge(service=service)

    try:
        driver.maximize_window()
        driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
            )

        waiter = WebDriverWait(driver, 10)

        # Заполнение полей
        driver.find_element(By.NAME, "first-name").send_keys("Иван")
        driver.find_element(By.NAME, "last-name").send_keys("Петров")
        driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
        driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
        driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
        # Zip code не заполняем
        driver.find_element(By.NAME, "city").send_keys("Москва")
        driver.find_element(By.NAME, "country").send_keys("Россия")
        driver.find_element(By.NAME, "job-position").send_keys("QA")
        driver.find_element(By.NAME, "company").send_keys("SkyPro")

        # Нажимаем Submit
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        # Ждем появления результатов
        waiter.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".alert.py-2")))

        # Проверяем zip-code (должен быть красный)
        zip_code_div = driver.find_element(By.ID, "zip-code")
        assert "alert-danger" in zip_code_div.get_attribute("class")

        # Проверяем остальные поля (должны быть зеленые)
        fields_to_check = [
            "first-name", "last-name", "address", "e-mail", "phone",
            "city", "country", "job-position", "company"
        ]

        for field_id in fields_to_check:
            field_div = driver.find_element(By.ID, field_id)
            assert "alert-success" in field_div.get_attribute("class")

    finally:
        driver.quit()


if __name__ == "__main__":
    pytest.main([__file__])
