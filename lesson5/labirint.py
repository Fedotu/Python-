# зайти на лабиринт
# найти книги по слову Python
# собирать все карточки товаров
# вывести в консоль инфо: название, автор, цена

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome(service=ChromeService
                          (ChromeDriverManager().install()))
driver.maximize_window()

# зайти на лабиринт
driver.get("https://www.labirint.ru/")

# найти книги по слову Python
search_field = "#search-field"
search_input = driver.find_element(By.CSS_SELECTOR, search_field)
search_input.send_keys("Python")
search_input.send_keys(Keys.ENTER)

sleep(2)

# собрать все карточки товара
books = driver.find_elements(By.CSS_SELECTOR, "div.product-card")
print(len(books))


# вывести в консоль инфо: название, автор, цена
for book in books:
    try:
        title = book.find_element(By.CSS_SELECTOR,
                                  "a.product-card__name").text
    except NoSuchElementException:
        title = "Название не указано"

    try:
        price = book.find_element(By.CSS_SELECTOR,
                                  "div.product-card__price-current").text
    except NoSuchElementException:
        price = "Цена не указана"

    try:
        author = book.find_element(By.CSS_SELECTOR,
                                   "div.product-card__author").text
    except NoSuchElementException:
        author = "Автор не указан"
    print(author + "\t" + title + "\t" + price)

sleep(10)
driver.quit()
