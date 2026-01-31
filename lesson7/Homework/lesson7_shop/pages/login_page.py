from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self._driver = driver

    def open(self):
        self._driver.get("https://www.saucedemo.com/")

    def login(self, username, password):
        self._driver.find_element(By.ID, "user-name").send_keys(username)
        self._driver.find_element(By.ID, "password").send_keys(password)
        self._driver.find_element(By.ID, "login-button").click()
