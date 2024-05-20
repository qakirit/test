import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class TestHome:

    @pytest.fixture(scope="class")
    def setup(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get("https://practicetestautomation.com/practice-test-login/")
        yield driver
        driver.quit()

    def test01(self, setup):
        driver = setup
        wait = WebDriverWait(driver, 10)
        title = "Test login"
        act_title = driver.find_element(By.XPATH, "//h2[text()='Test login']").text
        assert title == act_title, f"Expected title: '{title}' but found '{act_title}'."

    def test02(self, setup):
        driver = setup

        driver.find_element(By.ID, "username").send_keys("student")
        driver.find_element(By.ID, "password").send_keys("Password123")
        driver.find_element(By.ID, "submit").click()
        # Add assertions as needed
