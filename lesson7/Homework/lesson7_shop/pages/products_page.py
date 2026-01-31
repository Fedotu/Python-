from selenium.webdriver.common.by import By


class ProductsPage:
    def __init__(self, driver):
        self._driver = driver

    def add_to_cart(self, product_name):
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
            raise ValueError(f"Товар '{product_name}' не найден")

    def go_to_cart(self):
        self._driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
