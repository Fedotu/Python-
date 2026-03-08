import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.fixture
def driver():
    driver = webdriver.Firefox(service=FirefoxService(
        GeckoDriverManager(version="v0.34.0").install()
    ))
    driver.maximize_window()
    yield driver
    driver.quit()


def test_shopping_cart_total(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    products_page = ProductsPage(driver)
    products_page.add_to_cart("Sauce Labs Backpack")
    products_page.add_to_cart("Sauce Labs Bolt T-Shirt")
    products_page.add_to_cart("Sauce Labs Onesie")

    products_page.go_to_cart()

    cart_page = CartPage(driver)
    cart_page.checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.fill_shipping_info("Ekaterina", "Andrievskaya", "859684")

    total_text = checkout_page.get_total()
    assert total_text == "Total: $58.29"
