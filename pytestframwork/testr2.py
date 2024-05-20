import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class tet:
    @pytest.fixture(scope="class")
    def setup(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get("")

        yield driver

        driver.quit()

    def test01(self, setup):
        driver = setup
        driver.find_element(By.XPATH)

        wait = WebDriverWait(driver, 10)

        title = "Test login"
        act_title = driver.find_element(By.XPATH, "//h2[text()='Test login']").text
        assert title == act_title, f"Expected title: '{title}' but found '{act_title}'."

        assert title == act_title, f"Expected title:'{title}', but found '{act_title}'."

    def test02(self,setup):

        driver = setup
        tittle = "test"

        act_title = driver.find_element(By.XPATH,"")

        assert tittle == act_title,f"expected titlte,'{tittle}', but not found'{act_title}'"

    def test03(self,setup):
        driver = setup
