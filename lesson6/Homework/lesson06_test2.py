from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))
driver.get("http://uitestingplayground.com/textinput")

waiter = WebDriverWait(driver, 40)

search_field = "#search-field"
search_input = driver.find_element(By.ID, "newButtonName")
search_input.send_keys("SkyPro")
driver.find_element(By.ID, "updatingButton").click()

blue_element = driver.find_element(By.ID, "updatingButton")
txt = blue_element.text
print(txt)

driver.quit()
