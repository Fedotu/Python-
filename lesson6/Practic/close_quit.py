from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))
driver.get("http://www.uitestingplayground.com/ajax")
driver.implicitly_wait(20)  # драйвер жди, неявное ожидание
driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()


content = driver.find_element(By.CSS_SELECTOR, "#content")
txt = content.find_element(By.CSS_SELECTOR, "p.bg-success").text
print(txt)

sleep(5)

# driver.close()  # закрывает текущую вкладку
# driver.quit()  # закрывает весь браузер
