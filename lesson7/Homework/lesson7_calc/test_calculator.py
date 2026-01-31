import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from CalculatorPage import CalculatorPage


def test_calculator_45_seconds():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install())
    )

    try:
        calculator = CalculatorPage(driver)
        calculator.set_delay(45)

        # Нажимаем кнопки: 7, +, 8, =
        calculator.click_button(0)  # 7
        calculator.click_button(3)  # +
        calculator.click_button(1)  # 8
        calculator.click_button(14)  # =

        result = calculator.wait_for_result("15")
        assert result == "15"

    finally:
        driver.quit()


if __name__ == "__main__":
    pytest.main([__file__])
