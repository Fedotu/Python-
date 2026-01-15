# Поле ввода: ввести, удалить, ввести

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Firefox(service=FirefoxService(
    GeckoDriverManager(version="v0.34.0").install()  # укажи последнюю версию
))

# 1 не получилось скачать браузер, пробовала на другом
# 2 удалось скачать, но не работало
# 3 нашла решение, указав версию
# driver = webdriver.Firefox(service=FirefoxService
# (GeckoDriverManager().install()))
# driver = webdriver.Chrome(service=ChromeService
# (ChromeDriverManager().install()))
driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/inputs")

input_field = driver.find_element(By.CSS_SELECTOR, "input[type='number']")
input_field.send_keys("Sky")
input_field.clear()
input_field.send_keys("Pro")

sleep(3)

driver.quit()

# неполучилось сказать Firefox, проверку не прошла в Chrome
