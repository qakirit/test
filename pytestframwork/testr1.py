import pytest

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class test_home:
    @pytest.fixture(scope="class")
    def test_ser(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

        yield self.driver
        self.driver.quit()

    def test_launch(self,setup):
        driver = setup
        driver.get("https://www.flipkart.com/")

    def test_01(self,setup):
        driver = setup

    def test_02(self,setup):
        driver = setup
        wait = WebDriverWait(driver,10)
        wait.until(EC.element_to_be_clickable((By.XPATH,""))).click()



