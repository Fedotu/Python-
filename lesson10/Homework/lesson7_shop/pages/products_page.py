from selenium.webdriver.common.by import By
import allure


class ProductsPage:
    def __init__(self, driver) -> None:
        self._driver = driver

    @allure.step("Выбрать все товары слева")
    def add_to_cart(self, product_name: str) -> None:
        """Добавить товар в корзину по названию"""
        product_map = {
            "Sauce Labs Backpack": "add-to-cart-sauce-labs-backpack",
            "Sauce Labs Bolt T-Shirt": "add-to-cart-sauce-labs-bolt-t-shirt",
            "Sauce Labs Onesie": "add-to-cart-sauce-labs-onesie",
        }

        if product_name in product_map:
            self._driver.find_element(
                By.NAME, product_map[product_name]).click()
        else:
            # шаг, если произойдет ошибка
            with allure.step(f"Ошибка: товар '{product_name}' не найден"):
                raise ValueError(f"Товар '{product_name}' не найден")

    @allure.step("Нажать на иконку корзины")
    def go_to_cart(self) -> None:
        self._driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
