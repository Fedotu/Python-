from selenium.webdriver.common.by import By
import allure


class CartPage:
    def __init__(self, driver) -> None:
        self._driver = driver

    @allure.step("Нажать кнопку 'checkout'")
    def checkout(self) -> None:
        self._driver.find_element(By.ID, "checkout").click()
