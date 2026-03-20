from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CartPage:
    def __init__(self, driver) -> None:
        self._driver = driver
        self._waiter = WebDriverWait(self._driver, 10)

    @allure.step("Нажать кнопку 'checkout'")
    def checkout(self) -> None:
        checkout_btn = self._waiter.until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        )
        checkout_btn.click()
