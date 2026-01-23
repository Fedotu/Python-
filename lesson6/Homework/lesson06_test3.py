from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "landscape")))

award_img = driver.find_element(By.ID, "award")
print(award_img.get_attribute("src"))

driver.quit()
