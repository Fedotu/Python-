from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

award_img = WebDriverWait(driver, 10).until(
    lambda d: d.find_element(By.ID, "award")
)

print(award_img.get_attribute("src"))
driver.quit()
