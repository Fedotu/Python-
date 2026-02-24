from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

cookie = {
    "name": "cookie_policy",
    "value": "1"
    }


def test_card_counter():
    browser = webdriver.Chrome(
        service=ChromeService(
            ChromeDriverManager().install()))
    browser.get("https://www.labirint.ru/")
    browser.implicitly_wait(4)
    browser.maximize_window()
    browser.add_cookie(cookie)

    browser.find_element(By.CSS_SELECTOR, "#search-field").send_keys('python')
    browser.find_element(By.CSS_SELECTOR, "button[type=submit]").click()

# browser.find_element(By.CSS_SELECTOR, 'a[title="таблица"]').click()
# WebDriverWait(browser, 10).until(
# EC.presence_of_element_located((By.CSS_SELECTOR, "table"))
# )
    buy_buttons = browser.find_elements(
        By.CSS_SELECTOR, "[data-carttext]")
    counter = 0
    for btn in buy_buttons:
        btn.click()
        counter += 1

    browser.get("https://www.labirint.ru/cart/")

    txt = browser.find_element(By.ID, 'basket-default-prod-count2').text
    assert counter == int(txt.split()[0])
    browser.quit()
