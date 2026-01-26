from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
# не забудьте импортировать класс By
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))
driver.get("https://ya.ru")  # переход на сайт

element = driver.find_element(By.CSS_SELECTOR, "#text")  # поиск элемента

print(element)  # отображение результата в терминале

driver.quit()  # закрытие драйвера
