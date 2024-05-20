import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLogin:
    @pytest.fixture(scope="module")
    def setup(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        yield driver
        driver.quit()

    def test01_launch(self, setup):
        driver = setup
        driver.get("https://practicetestautomation.com/practice-test-login/")

        driver.find_element(By.ID, "username").send_keys("student")

        driver.find_element(By.ID, "password").send_keys("Password123")

        driver.find_element(By.ID, "submit").click()
