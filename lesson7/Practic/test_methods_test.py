from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

cookie = {
    "name": "cookie_policy",
    "value": "1"
    }

browser = webdriver.Chrome()


def open_labirint():
    browser.get("https://www.labirint.ru/")
    browser.implicitly_wait(4)
    browser.maximize_window()
    browser.add_cookie(cookie)


def search(term):
    browser.find_element(
        By.CSS_SELECTOR, "#search-field").send_keys(term)
    browser.find_element(By.CSS_SELECTOR, "button[type=submit]").click()


def add_books():
    buy_buttons = browser.find_elements(
        By.CSS_SELECTOR, "[data-carttext]")

    counter = 0
    for btn in buy_buttons:
        btn.click()
        counter += 1

    return counter


def go_to_card():
    browser.get("https://www.labirint.ru/cart/")


def get_cart_counter():
    txt = browser.find_element(
        By.CSS_SELECTOR, 'a]data-event-labek="myCart"]'
        ).find_element(By.CSS_SELECTOR, 'b').text
    return int(txt.split()[0])


def close_driver():
    browser.quit()


def test_methods_test():
    open_labirint()
    search('python')
    added = add_books()
    go_to_card()
    cart_counter = get_cart_counter()
    close_driver()
    assert added == cart_counter
