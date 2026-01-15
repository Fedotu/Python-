from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

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

driver.get("http://the-internet.herokuapp.com/login")

username_field = driver.find_element(By.CSS_SELECTOR, "input#username")
username_field.send_keys("tomsmith")

password_field = driver.find_element(By.CSS_SELECTOR, "input#password")
password_field.send_keys("SuperSecretPassword!")

login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
login_button.click()

sleep(2)

success_message = driver.find_element(By.CSS_SELECTOR, ".flash.success")
print("Текст из зеленой плашки:", success_message.text)

sleep(3)
driver.quit()

# неполучилось сказать Firefox, проверку прошла в Chrome
