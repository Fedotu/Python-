from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import allure


class CheckoutPage:
    def __init__(self, driver) -> None:
        self._driver = driver
        self._waiter = WebDriverWait(self._driver, 10)

    @allure.step("Ввести данные пользователя")
    def fill_shipping_info(
            self, first_name: str, last_name: str, postal_code: str) -> None:
        self._driver.find_element(By.ID, "first-name").send_keys(first_name)
        self._driver.find_element(By.ID, "last-name").send_keys(last_name)
        self._driver.find_element(By.ID, "postal-code").send_keys(postal_code)

    @allure.step("Нажать кнопку 'continue'")
    def continue_cl(self) -> None:
        self._driver.find_element(By.ID, "continue").click()
