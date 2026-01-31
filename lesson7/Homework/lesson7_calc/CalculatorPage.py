from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/"
                         "slow-calculator.html")

    def set_delay(self, delay):
        delay_input = self._driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys(str(delay))

    def click_button(self, button_index):
        buttons = self._driver.find_elements(By.CSS_SELECTOR, ".keys span")
        buttons[button_index].click()

    def get_result(self):
        screen = self._driver.find_element(By.CLASS_NAME, "screen")
        return screen.text

    def wait_for_result(self, expected, timeout=50):
        wait = WebDriverWait(self._driver, timeout)
        wait.until(EC.text_to_be_present_in_element(
            (By.CLASS_NAME, "screen"), str(expected)))
        return self.get_result()
