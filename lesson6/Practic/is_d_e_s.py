# is_displayed

# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By

# driver = webdriver.Chrome
# service=ChromeService(ChromeDriverManager().install()))

# driver.get("http://uitestingplayground.com/visibility")
# is_displayed = driver.find_element(
# By.CSS_SELECTOR, "#transparentButton").is_displayed()

# print(is_displayed)  # вывод статуса видимости Opacity 0\

# нажатие на Hide
# driver.find_element(By.CSS_SELECTOR, "#hideButton").click()

# Opacity 0 окажется скрытой
# sleep(2)

# еще раз проверим видимость Opacity 0:
# is_displayed = driver.find_element(
# By.CSS_SELECTOR, "#transparentButton").is_displayed()

# print(is_displayed)  # еще раз выводим статус видимости Opacity 0
# sleep(2)

# driver.quit()


# is_enabled
# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By

# driver = webdriver.Chrome(
# service=ChromeService(ChromeDriverManager().install()))

# driver.get("https://demoqa.com/radio-button")

# is_enabled = driver.find_element(By.CSS_SELECTOR, "#yesRadio").is_enabled()
# print(is_enabled)

# is_enabled = driver.find_element(By.CSS_SELECTOR, "#noRadio").is_enabled()
# print(is_enabled)

# driver.quit()


# (is_selected)
# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By

# driver = webdriver.Chrome(
# service=ChromeService(ChromeDriverManager().install()))

# driver.get("https://the-internet.herokuapp.com/checkboxes")

# cb = driver.find_element(By.CSS_SELECTOR, "input[type=checkbox]")

# is_selected = cb.is_selected()
# print(is_selected)
# sleep(3)

# cb.click()

# is_selected = cb.is_selected()
# print(is_selected)
# sleep(3)

# driver.quit()
