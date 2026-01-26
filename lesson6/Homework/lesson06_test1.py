from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))
driver.get("http://uitestingplayground.com/ajax")

waiter = WebDriverWait(driver, 40)

driver.find_element(By.ID, "ajaxButton").click()
waiter.until(EC.presence_of_element_located((By.CLASS_NAME, "bg-success")))
green_element = driver.find_element(By.CLASS_NAME, "bg-success")
txt = green_element.text

print(txt)

driver.quit()
