import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec


class TestLoginPage:
    @pytest.fixture(scope="class")
    def setup(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        yield driver
        driver.quit()

    def test_valid_login(self, setup):
        driver = setup
        driver.get("https://practicetestautomation.com/practice-test-login/")
        username_input = driver.find_element(By.ID, "username")
        password_input = driver.find_element(By.ID, "password")
        submit_button = driver.find_element(By.ID, "submit")

        username_input.send_keys("student")
        password_input.send_keys("Password123")
        submit_button.click()

        expected_message = "Logged In Successfully"
        wait = WebDriverWait(driver, 10)
        actual_message = wait.until(Ec.visibility_of_element_located((By.XPATH, "//h1[@class='post-title']"))).text
        assert expected_message == actual_message

    def test_invalid_login(self, setup):
        driver = setup
        driver.get("https://practicetestautomation.com/practice-test-login/")
        username_input = driver.find_element(By.ID, "username")
        password_input = driver.find_element(By.ID, "password")
        submit_button = driver.find_element(By.ID, "submit")

        username_input.send_keys("invalid_user")
        password_input.send_keys("invalid_password")
        submit_button.click()

        expected_message = "Your username is invalid!"
        wait = WebDriverWait(driver, 10)
        actual_message = wait.until(Ec.visibility_of_element_located((By.ID, "error"))).text
        assert expected_message == actual_message

    def test_empty_login_fields(self, setup):
        driver = setup
        driver.get("https://practicetestautomation.com/practice-test-login/")
        submit_button = driver.find_element(By.ID, "submit")

        submit_button.click()

        expected_message = "Your username is invalid!"
        wait = WebDriverWait(driver, 10)
        actual_message = wait.until(Ec.visibility_of_element_located((By.ID, "error"))).text
        assert expected_message == actual_message
