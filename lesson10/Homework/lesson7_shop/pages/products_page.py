from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class ProductsPage:
    def __init__(self, driver) -> None:
        self._driver = driver
        self._waiter = WebDriverWait(self._driver, 10)

    @allure.step("Выбрать все товары слева")
    def add_to_cart(self, product_name: str) -> None:
        """Добавить товар в корзину по названию"""
        product_map = {
            "Sauce Labs Backpack": "add-to-cart-sauce-labs-backpack",
            "Sauce Labs Bolt T-Shirt": "add-to-cart-sauce-labs-bolt-t-shirt",
            "Sauce Labs Onesie": "add-to-cart-sauce-labs-onesie",
        }

        if product_name in product_map:
            element = self._waiter.until(
                EC.element_to_be_clickable(
                    (By.NAME, product_map[product_name])))
            element.click()
        else:
            # шаг, если произойдет ошибка
            with allure.step(f"Ошибка: товар '{product_name}' не найден"):
                raise ValueError(f"Товар '{product_name}' не найден")

    @allure.step("Нажать на иконку корзины")
    def go_to_cart(self) -> None:
        cart_icon = self._waiter.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link")))
        cart_icon.click()
