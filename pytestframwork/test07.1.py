import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec

@pytest.fixture(scope="function")
def setup(request):
    driver = webdriver.Firefox()
    driver.maximize_window()

    yield driver
    driver.quit()

@pytest.mark.parametrize("username, password, expected_message", [
    ("valid_username", "valid_password", "Logged In Successfully"),
    ("invalid_username", "invalid_password", "Your username is invalid!"),
    # Add more test cases here as needed
])
def test_login(setup, username, password, expected_message):
    driver = setup
    driver.get("https://practicetestautomation.com/practice-test-login/")
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "submit").click()

    wait = WebDriverWait(driver, 10)
    actual_message = wait.until(Ec.visibility_of_element_located((By.ID, "error"))).text
    assert actual_message == expected_message
