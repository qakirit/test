from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


class TestLogin:

    @pytest.fixture(scope="class")
    def setup(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        yield driver
        driver.quit()

    @pytest.mark.parametrize("username, password, expected_message", [
        ("student", "Password123", "Home"),
        ("student", "Password123", "Home")
    ])
    def test_login(self, setup, username, password, expected_message):
        driver = setup
        driver.get("https://practicetestautomation.com/practice-test-login/")
        username_field = driver.find_element(By.ID, "username")
        username_field.send_keys(username)
        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys(password)

        driver.find_element(By.ID, "submit").click()

        # Assert that the expected message is present on the page
        welcome_message = driver.find_element(By.XPATH, f"//a[text()='{expected_message}']")
        assert welcome_message.is_displayed(), f"Expected message '{expected_message}' not found on the page"
