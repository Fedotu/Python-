from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))
driver.get("https://ya.ru")

# usd = driver.find_element(By.CSS_SELECTOR,
# '[data-statlog="2informers.stocks.item.1"]')
# txt = usd.text
# в переменную с методом text соберется информация об элементе

txt = driver.find_element(By.CSS_SELECTOR, "a[title='USD MOEX]").text
print(txt)

tag = driver.find_element(By.CSS_SELECTOR, "a[title='USD MOEX]").tag_name
print(tag)

id = driver.find_element(By.CSS_SELECTOR, "a[title='USD MOEX]").id
print(id)

href = driver.find_element(By.CSS_SELECTOR,
                           "a[title='USD MOEX]").get_attribute("href")
print(href)

ff = (driver.find_element(By.CSS_SELECTOR,
                          '[data-statlog="2informers.stocks.item.1"]'
                          ).value_of_css_property("font-family"))
print(ff)

# print(txt)  # запрос выведет информацию из переменной в терминал
sleep(5)
driver.quit()  # закрываем драйвер
