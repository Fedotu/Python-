from selenium.webdriver.common.by import By
import allure


class LoginPage:
    def __init__(self, driver) -> None:
        self._driver = driver

    @allure.step("Открыть сайт магазина")
    def open(self) -> None:
        self._driver.get("https://www.saucedemo.com/")

    @allure.step("Ввести логин, пароль и нажать 'login'")
    def login(self, username: str, password: str) -> None:
        self._driver.find_element(By.ID, "user-name").send_keys(username)
        self._driver.find_element(By.ID, "password").send_keys(password)
        self._driver.find_element(By.ID, "login-button").click()
