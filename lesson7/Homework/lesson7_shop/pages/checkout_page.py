from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    def __init__(self, driver):
        self._driver = driver
        self._waiter = WebDriverWait(self._driver, 10)

    def fill_shipping_info(self, first_name, last_name, postal_code):
        self._driver.find_element(By.ID, "first-name").send_keys(first_name)
        self._driver.find_element(By.ID, "last-name").send_keys(last_name)
        self._driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        self._driver.find_element(By.ID, "continue").click()

    def get_total(self):
        self._waiter.until(EC.text_to_be_present_in_element(
            (By.CLASS_NAME, "summary_total_label"), "$"))

        total_element = self._driver.find_element(
            By.CLASS_NAME, "summary_total_label")
        return total_element.text
